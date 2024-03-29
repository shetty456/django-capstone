from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('items/', views.MenuItemView.as_view()),
    path('items/<int:pk>', views.SingleMenuItemView.as_view())
]
