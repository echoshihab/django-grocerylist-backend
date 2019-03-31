from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroceryList.as_view()),
    path('<int:pk>/', views.GroceryItem.as_view()),

]
