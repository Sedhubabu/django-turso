# mysite/urls.py

from django.urls import path
from app.views import items, add_user, list_users

urlpatterns = [
    path('items/', items),
    path('users/add/', add_user),
    path('users/', list_users),
]
