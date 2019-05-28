from django.shortcuts import render

# Create your views here.
from rest_framework import generics, permissions
from .models import Grocerylist
from .serializers import GroceryListSerializer


class GroceryList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroceryListSerializer

    def get_queryset(self):
        return self.request.user.grocerylist.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GroceryItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = GroceryListSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return self.request.user.grocerylist.all()
