import graphene

from ingredients.models import Category
from ingredients.serializers import (
    CategoryNode,
    CreateCategoryModel,
    UpdateCategoryModel,
)


class CreateCategory(graphene.Mutation):
    class Arguments:
        category_data = graphene.Argument(CreateCategoryModel)

    category = graphene.Field(CategoryNode)

    def mutate(self, info, category_data: CreateCategoryModel):
        c = Category(
            name=category_data.name,
        )
        c.save()
        return CreateCategory(category=c)


class UpdateCategory(graphene.Mutation):
    class Arguments:
        category_data = graphene.Argument(UpdateCategoryModel)

    category = graphene.Field(CategoryNode)

    def mutate(self, info, category_data: UpdateCategoryModel):
        c = Category.objects.get(pk=category_data.id)
        c.name = str(category_data.name)
        c.save()
        return UpdateCategory(category=c)
