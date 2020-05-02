from django.urls import path
from recipe import views

urlpatterns = [
    path('', views.index, name='home'),
    path('recipe/<int:id>', views.recipe, name='recipe'),
    path('author/<int:id>', views.author, name='author'),
]
