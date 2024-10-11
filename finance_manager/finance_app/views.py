from django.shortcuts import render
from .models import TodoItem, AppItem

# Create your views here.
def home(request):
    items = AppItem.objects.all()
    return render(request, "home.html", {"apps": items})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})