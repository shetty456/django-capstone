from rest_framework.serializers import ModelSerializer
from restaurant.models import Menu, Booking


class MenuItemSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = ["title", "price", "inventory"]


class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
