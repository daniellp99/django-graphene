import graphene

from core.query import Query

schema = graphene.Schema(query=Query)
