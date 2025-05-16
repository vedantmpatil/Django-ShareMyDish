from django.urls import path
from . import views

app_name = 'dish'

urlpatterns = [
    path('', views.explore, name='explore'),
    path('recipes/', views.recipes, name='all_recipes'),
    path('recipes/<int:pk>/', views.recipe_detail, name='recipe_detail'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('update/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('delete/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('about/', views.about, name='about'),
]
