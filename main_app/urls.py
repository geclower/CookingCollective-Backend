from django.urls import path
from .views import Home, RecipeList, RecipeDetail, RecipeByFoodCat, RecipeByMealCat

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:id>/', RecipeDetail.as_view(), name='recipe-detail'),

    path('recipes/food/<str:food_id>', RecipeByFoodCat.as_view(), name='recipe-food-list'),
    path('recipes/meal/<str:meal_id>', RecipeByMealCat.as_view(), name='recipe-meal-list'),
]