from django.db import models

# Create your models here.


class Grocerylist(models.Model):
    item = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200, default=1)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.item
