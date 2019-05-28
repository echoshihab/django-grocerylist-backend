from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Grocerylist(models.Model):
    item = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, default=1)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(
        User, related_name="grocerylist", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.item
