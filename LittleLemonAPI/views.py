from django.shortcuts import render
from .models import MenuItem
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
)
from .serializers import MenuItemSerializer


# Create your views here.
class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
