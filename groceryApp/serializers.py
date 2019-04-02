from rest_framework import serializers
from .models import Grocerylist


class GroceryListSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'item',
            'quantity',
            'completed',
        )
        model = Grocerylist
