from django.conf import settings

import graphene

from . import base


class Settings(base.Settings):
    def __init__(self, *args, **kwargs):
        if hasattr(settings, "GRAPHENE_PROTECTOR_DEPTH_LIMIT"):
            kwargs.setdefault(
                "depth_limit", settings.GRAPHENE_PROTECTOR_DEPTH_LIMIT
            )
        if hasattr(settings, "GRAPHENE_PROTECTOR_SELECTIONS_LIMIT"):
            kwargs.setdefault(
                "selections_limit",
                settings.GRAPHENE_PROTECTOR_SELECTIONS_LIMIT
            )
        if hasattr(settings, "GRAPHENE_PROTECTOR_COMPLEXITY_LIMIT"):
            kwargs.setdefault(
                "complexity_limit",
                settings.GRAPHENE_PROTECTOR_COMPLEXITY_LIMIT
            )
        super().__init__(*args, **kwargs)


class Limits(base.Limits, settings=Settings()):
    pass


class ProtectorBackend(base.ProtectorBackend):
    def __init__(self, *args, **kwargs):
        limits = Limits()
        kwargs.setdefault("depth_limit", limits.depth)
        kwargs.setdefault("selections_limit", limits.selections)
        kwargs.setdefault("complexity_limit", limits.complexity)
        super().__init__(*args, **kwargs)


class Schema(graphene.Schema):
    def __init__(self, *args, **kwargs):
        self.backend = kwargs.pop("backend", ProtectorBackend())
        super().__init__(*args, **kwargs)

    def execute(self, *args, **kwargs):
        kwargs.setdefault("backend", self.backend)
        return super().execute(*args, **kwargs)
