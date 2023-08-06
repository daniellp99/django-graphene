import graphene

from ingredients.models import Category, Ingredient
from ingredients.serializers import (
    CreateIngredientModel,
    IngredientNode,
    UpdateIngredientModel,
)


class CreateIngredient(graphene.Mutation):
    class Arguments:
        ingredient_data = graphene.Argument(CreateIngredientModel)

    ingredient = graphene.Field(IngredientNode)

    def mutate(self, info, ingredient_data: CreateIngredientModel):
        category_data = Category.objects.get(pk=ingredient_data.category_id)
        i = Ingredient(
            name=ingredient_data.name,
            notes=ingredient_data.notes,
            category=category_data,
        )
        i.save()
        return CreateIngredient(ingredient=i)


class UpdateIngredient(graphene.Mutation):
    class Arguments:
        ingredient_data = graphene.Argument(UpdateIngredientModel)

    ingredient = graphene.Field(IngredientNode)

    def mutate(self, info, ingredient_data: UpdateIngredientModel):
        category = Category.objects.get(id=ingredient_data.category_id)
        i = Ingredient.objects.get(id=ingredient_data.id)
        i.name = str(ingredient_data.name)
        i.notes = str(ingredient_data.notes)
        i.category = category
        i.save()
        return UpdateIngredient(ingredient=i)
