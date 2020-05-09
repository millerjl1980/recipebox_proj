from django import forms
from django.forms import modelform_factory
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from recipe.models import Author, Recipe

# Since there were no fields in the models that were goiing to be excluded
# used modelform_factory to make forms with


AddRecipeForm = modelform_factory(Recipe, exclude=[])

# AddAuthorForm = modelform_factory(Author, exclude=['user'])

class AddAuthorForm(UserCreationForm):
    name = forms.CharField(max_length=50)
    bio = forms.CharField()
    class Meta:
        model = User
        fields = ('name', 'bio', 'username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)