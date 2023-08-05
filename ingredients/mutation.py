import graphene

from ingredients.mutations.ingredient import CreateIngredient, UpdateIngredient


class Mutations(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field(description="Create Ingredient")
    update_ingredient = UpdateIngredient.Field(description="Update Ingredient")
