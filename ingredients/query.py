import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from ingredients.serializers import (
    CategoryNode,
    IngredientNode,
)


class Queries(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
