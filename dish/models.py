from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Item model for each dish - id (auto) , item_name, item_ingredients, item_image_url, item_recipie, item_cooking_time, item_cuisine, item_author, item_video_url, item_difficulty, item_type
class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_ingredients = models.TextField()
    item_image_url = models.CharField(max_length=500)
    item_recipe = models.TextField()
    item_cooking_time = models.IntegerField()
    item_cuisine = models.CharField(max_length=200)
    item_author = models.CharField(max_length=200)
    item_video_url = models.CharField(max_length=500)
    item_difficulty = models.CharField(max_length=50)
    item_type = models.CharField(max_length=50)

    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes', default=None)

