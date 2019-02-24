from django.conf.urls import include
from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('course', views.CourseViewSet)
router.register('cuisine', views.CuisineViewSet)
router.register('source_display_name', views.SourceViewSet)
router.register('recipe', views.RecipeViewSet)
router.register('course_recipe', views.CourseRecipeViewSet)
router.register('cuisine_recipe', views.CuisineRecipeViewSet)
router.register('flavor', views.FlavorViewSet)
router.register('ingredient', views.IngredientViewSet)
router.register('ingredient_recipe', views.IngredientRecipeViewSet)

urlpatterns = [
    path('', include(router.urls))
]