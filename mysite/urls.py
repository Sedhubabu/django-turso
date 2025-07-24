# mysite/urls.py

from django.urls import path
from app.views import items, add_user, list_users
from django.http import HttpResponse
def home(request):
    return HttpResponse("Hello from Railway!")

urlpatterns = [
    path('items/', items),
    path('',home),
    path('users/add/', add_user),
    path('users/', list_users),
]
