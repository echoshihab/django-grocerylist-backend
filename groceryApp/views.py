from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Grocerylist
from .serializers import GroceryListSerializer


class GroceryList(generics.ListCreateAPIView):
    queryset = Grocerylist.objects.all()
    serializer_class = GroceryListSerializer


class GroceryItem(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grocerylist.objects.all()
    serializer_class = GroceryListSerializer
