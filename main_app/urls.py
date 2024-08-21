from django.urls import path
from .views import Home, RecipeList, RecipeDetail

urlpatterns = [
    path('', Home.as_view(), name='home'),

    path('recipes/', RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:id>/', RecipeDetail.as_view(), name='recipe-detail')
]