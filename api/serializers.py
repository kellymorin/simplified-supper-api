from rest_framework import serializers
from api.models import *

class CourseSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"

class CuisineSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cuisine
        fields = "__all__"

class SourceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Source_Display_Name
        fields = "__all__"

class RecipeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Recipe
        fields = "__all__"

class CourseRecipeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Course_Recipe
        fields = "__all__"

class CuisineRecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cuisine_Recipe
        fields = "__all__"

class FlavorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flavors
        fields = "__all__"

class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients
        fields = "__all__"

class IngredientRecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingredients_Recipe
        fields = "__all__"