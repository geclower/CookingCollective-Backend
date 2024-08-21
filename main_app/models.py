from django.db import models
from django.contrib.postgres.fields import ArrayField

CATEGORIES = (
    ('beef', 'Beef'),
    ('chic', 'Chicken'),
    ('dess', 'Dessert'),
    ('lamb', 'Lamb'),
    ('misc', 'Miscellaneous'),
    ('past', 'Pasta'),
    ('pork', 'Pork'),
    ('seaf', 'Seafood'),
    ('side', 'Side'),
    ('star', 'Starter'),
    ('vega', 'Vegan'),
    ('vege', 'Vegetarian'),
    ('brea', 'Breakfast'),
    ('goat', 'Goat'),
)

class Recipe(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=4, choices=CATEGORIES, default=CATEGORIES[0][0])
    instructions = models.TextField()
    image = models.CharField()
    video = models.CharField()
    ingredients = ArrayField(models.CharField(), blank=True, null=True)
    source = models.CharField()

    def __str__(self):
        return self.name