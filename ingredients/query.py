import graphene
from graphene import relay
from graphene_django.filter import DjangoFilterConnectionField

from ingredients.models import Category, Ingredient
from ingredients.serializers import (
    CategoryNode,
    CategoryType,
    IngredientNode,
    IngredientType,
)


class Queries(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    all_ingredients_by_type = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients_by_type(self, root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(self, root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None

    category = relay.Node.Field(CategoryNode)
    all_categories = DjangoFilterConnectionField(CategoryNode)

    ingredient = relay.Node.Field(IngredientNode)
    all_ingredients = DjangoFilterConnectionField(IngredientNode)
