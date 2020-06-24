from django.forms import modelform_factory
from recipe.models import Author, Recipe

# Since there were no fields in the models that were goiing to be excluded
# used modelform_factory to make forms with

AddAuthorForm = modelform_factory(Author, exclude=[])

AddRecipeForm = modelform_factory(Recipe, exclude=[])
