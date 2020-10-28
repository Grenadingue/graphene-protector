# What does this project solve?

It is a small backend for a graphql schema which protects against malicious requests.

The current logic is simple and efficient (early bail out)

# Installation
````
pip install graphene-protector
````

# Integration

## Django
This adds to django following settings:
* GRAPHENE\_PROTECTOR\_DEPTH\_LIMIT: max depth
* GRAPHENE\_PROTECTOR\_SELECTIONS\_LIMIT: max selections
* GRAPHENE\_PROTECTOR\_COMPLEXITY\_LIMIT: max (depth * selections)

Integrate with:
```` python 3
# schema.py
# replace normal Schema import with:
from graphene_protector.django import Schema
````

manual way

```` python 3
from graphene import Schema
from graphene_protector.django import ProtectorBackend
backend = ProtectorBackend()
schema = graphene.Schema(query=Query)
result = schema.execute(query_string, backend=backend)

````

## Other/Manually
Following extra keyword arguments are supported:
* depth_limit: max depth
* selections_limit: max selections
* complexity_limit: max (depth * selections)

they overwrite django settings if specified

```` python 3
from graphene_protector import ProtectorBackend
backend = ProtectorBackend(depth_limit=10, selections_limit=None, complexity_limit=100)
schema = graphene.Schema(query=Query)
result = schema.execute(query_string, backend=backend)

````


# Development
I am open for new ideas.
If you want some new or better algorithms integrated just make a PR


# related projects:
* secure-graphene: lacks django integration and more sophisticated query limitations and yeah the not invented here syndrom
