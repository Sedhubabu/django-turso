from django.http import JsonResponse
from .turso_ops import list_items, create_item

def items(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        desc = request.POST.get("description", "")
        itm = create_item(name, desc)
        return JsonResponse({"id": itm.id, "name": itm.name, "description": itm.description})
    else:
        data = [{"id": i.id, "name": i.name, "description": i.description} for i in list_items()]
        return JsonResponse(data, safe=False)
# app/views.py

from django.http import JsonResponse
from .models_sqla import SessionLocal, Item, User
# app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models_sqla import User
from app.db import SessionLocal

def add_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')

        session = SessionLocal()
        user = User(username=username, email=email)
        session.add(user)
        session.commit()
        return JsonResponse({'status': 'User created'})
    
    return render(request, 'add_user.html')


def list_users(request):
    session = SessionLocal()
    users = session.query(User).all()
    return JsonResponse({'users': [{'id': u.id, 'username': u.username, 'email': u.email} for u in users]})
