from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.models import *
from api.serializers import *

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'course': reverse('course', request=request, format=format),
        'cuisine': reverse('cuisine', request=request, format=format),
        'source_display_name': reverse('source_display_name', request=request, format=format),
        'recipe': reverse('recipe', request=request, format=format),
        'course_recipe': reverse('course_recipe', request=request, format=format),
        'cuisine_recipe': reverse('cuisine_recipe', request=request, format=format),
        'flavors': reverse('flavors', request=request, format=format),
        'ingredients': reverse('ingredients', request=request, format=format),
        'ingredient_recipe': reverse('ingredient_recipe', request=request, format=format)
    })

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CuisineViewSet(viewsets.ModelViewSet):
    queryset = Cuisine.objects.all()
    serializer_class = CuisineSerializer

class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source_Display_Name.objects.all()
    serializer_class = SourceSerializer

class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class CourseRecipeViewSet(viewsets.ModelViewSet):
    queryset = Course_Recipe.objects.all()
    serializer_class = CourseRecipeSerializer

class CuisineRecipeViewSet(viewsets.ModelViewSet):
    queryset = Cuisine_Recipe.objects.all()
    serializer_class = CuisineRecipeSerializer

class FlavorViewSet(viewsets.ModelViewSet):
    queryset = Flavors.objects.all()
    serializer_class = FlavorSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredients.objects.all()
    serializer_class = IngredientSerializer

class IngredientRecipeViewSet(viewsets.ModelViewSet):
    queryset = Ingredients_Recipe.objects.all()
    serializer_class = IngredientRecipeSerializer

