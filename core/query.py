import graphene

from ingredients.models import Category, Ingredient
from ingredients.serializers import CategoryType, IngredientType


class Query(graphene.ObjectType):
    hello = graphene.String(default_value="Hi!")

    all_ingredients = graphene.List(IngredientType)
    category_by_name = graphene.Field(CategoryType, name=graphene.String(required=True))

    def resolve_all_ingredients(self, root, info):
        # We can easily optimize query count in the resolve method
        return Ingredient.objects.select_related("category").all()

    def resolve_category_by_name(self, root, info, name):
        try:
            return Category.objects.get(name=name)
        except Category.DoesNotExist:
            return None
