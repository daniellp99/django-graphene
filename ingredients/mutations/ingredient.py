import graphene
from ingredients.models import Ingredient

from ingredients.serializers import (
    CreateIngredientModel,
    IngredientNode,
    UpdateIngredientModel,
)


class CreateIngredient(graphene.Mutation):
    def __init__(self, ingredient=None):
        self.ingredient = ingredient

    class Arguments:
        ingredient_data = graphene.Argument(CreateIngredientModel)

    ingredient = graphene.Field(IngredientNode)

    def mutate(self, cls, info, ingredient_data: CreateIngredientModel):
        ingredient = Ingredient(
            name=ingredient_data.name,
            notes=ingredient_data.notes,
        )
        ingredient.save()
        return CreateIngredient(ingredient=ingredient)


class UpdateIngredient(graphene.Mutation):
    def __init__(self, ingredient=None):
        self.ingredient = ingredient

    class Arguments:
        ingredient_data = graphene.Argument(UpdateIngredientModel)

    ingredient = graphene.Field(IngredientNode)

    def mutate(self, cls, info, ingredient_data: UpdateIngredientModel):
        ingredient = Ingredient.objects.get(id=ingredient_data.id)
        ingredient.name = str(ingredient.name)
        ingredient.notes = str(ingredient.notes)
        ingredient.save()
        return UpdateIngredient(ingredient=ingredient)
