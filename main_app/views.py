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
    
class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    lookup_field = 'id'