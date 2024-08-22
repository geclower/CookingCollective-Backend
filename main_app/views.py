from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from .models import Recipe
from .serializers import RecipeSerializer

class Home(APIView):
    def get(self,request):
        content = {'message': 'Welcome to the recipes api home route!'}
        return Response(content)

# get all recipes
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

# get a single recipe by id
class RecipeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'

# get all recipes within a food category
class RecipeByFoodCat(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    def get_queryset(self):
        food_id = self.kwargs['food_id']
        return Recipe.objects.filter(category_food=food_id)

# get all recipes within a meal category
class RecipeByMealCat(generics.ListCreateAPIView):
    serializer_class = RecipeSerializer
    def get_queryset(self):
        meal_id = self.kwargs['meal_id']
        return Recipe.objects.filter(category_meal=meal_id)