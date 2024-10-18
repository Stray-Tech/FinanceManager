from django.shortcuts import render
from .models import TodoItem, AppItem, UserInput

# Create your views here.
def home(request):
    items = AppItem.objects.all()
    user_form = UserInput
    return render(request, "home.html", {"apps": items, "form": user_form})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def test(request):
    return render(request, "test.html")