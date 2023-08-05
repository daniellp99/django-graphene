from graphene import InputObjectType, Int, String, relay
from graphene_django import DjangoObjectType

from ingredients.models import Category, Ingredient


class CategoryNode(DjangoObjectType):
    class Meta:
        model = Category
        filter_fields = ["name", "ingredients"]
        interfaces = (relay.Node,)


class IngredientNode(DjangoObjectType):
    class Meta:
        model = Ingredient
        # Allow for some more advanced filtering here
        filter_fields = {
            "name": ["exact", "icontains", "istartswith"],
            "notes": ["exact", "icontains"],
            "category": ["exact"],
            "category__name": ["exact"],
        }
        interfaces = (relay.Node,)


class CategoryConnection(relay.Connection):
    class Meta:
        node = CategoryNode


class IngredientConnection(relay.Connection):
    class Meta:
        node = IngredientNode


class CreateIngredientModel(InputObjectType):
    name = String(required=True)
    notes = String(required=True)


class UpdateIngredientModel(CreateIngredientModel):
    id = Int(required=True)
