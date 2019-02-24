from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cuisine(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Source_Display_Name(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    recipe_details_url = models.CharField(max_length=500)
    total_time_in_seconds = models.PositiveIntegerField()
    rating = models.PositiveIntegerField()
    source_display_name = models.ForeignKey(Source_Display_Name,on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Course_Recipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.recipe.name} {self.course.name}"

class Cuisine_Recipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    cuisine = models.ForeignKey(Cuisine, on_delete = models.PROTECT)

    def __str__(self):
        return f"{self.recipe.name} {self.cuisine.name}"

class Flavors(models.Model):
    piquant = models.IntegerField()
    meaty = models.IntegerField()
    bitter = models.IntegerField()
    sweet = models.IntegerField()
    sour = models.IntegerField()
    salty = models.IntegerField()
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)

    def __str__(self):
        return self.piquant

class Ingredients(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Ingredients_Recipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.PROTECT)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.recipe.name} {self.ingredient.name}"


