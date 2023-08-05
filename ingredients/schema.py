import graphene

from .query import Queries
from .mutation import Mutations

schema = graphene.Schema(query=Queries, mutation=Mutations)
