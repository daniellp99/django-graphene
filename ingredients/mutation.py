import graphene

from ingredients.mutations.category import CreateCategory, UpdateCategory
from ingredients.mutations.ingredient import CreateIngredient, UpdateIngredient


class Mutations(graphene.ObjectType):
    create_ingredient = CreateIngredient.Field(description="Create Ingredient")
    update_ingredient = UpdateIngredient.Field(description="Update Ingredient")
    create_category = CreateCategory.Field(description="Create Category")
    update_category = UpdateCategory.Field(description="Update Category")
