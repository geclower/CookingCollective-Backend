from django.db import models
from django.contrib.postgres.fields import ArrayField

CATEGORIES_FOOD = (
    ('beef', 'Beef'),
    ('chic', 'Chicken'),
    ('lamb', 'Lamb'),
    ('othe', 'Other'),
    ('past', 'Pasta'),
    ('pork', 'Pork'),
    ('seaf', 'Seafood'),
    ('vega', 'Vegan'),
    ('vege', 'Vegetarian'),
    ('goat', 'Goat'),
)

CATEGORIES_MEAL = (
    ('brea', 'Breakfast'),
    ('ludi', 'Lunch/Dinner'),
    ('dess', 'Dessert'),
    ('side', 'Side'),
    ('star', 'Starter'),
)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category_food = models.CharField(max_length=4, choices=CATEGORIES_FOOD, default=CATEGORIES_FOOD[0][0])
    category_meal = models.CharField(max_length=4, choices=CATEGORIES_MEAL, default=CATEGORIES_MEAL[0][0])
    instructions = models.TextField()
    image = models.CharField(blank=True)
    video = models.CharField(blank=True)
    ingredients = ArrayField(models.CharField(), blank=True, null=True)
    source = models.CharField(blank=True)

    def __str__(self):
        return self.name