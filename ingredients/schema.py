
import graphene

from .query import Queries

schema = graphene.Schema(
    query=Queries,
)
