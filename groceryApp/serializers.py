from rest_framework import serializers
from .models import Grocerylist


class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grocerylist
        fields = '__all__'
