from django.shortcuts import render
from .models import TodoItem, AppItem
from .forms import UserInput
from .templatetags.filters import add_class

# Create your views here.
def home(request):
    items = AppItem.objects.all()
    user_form = UserInput()
    #add_class = add_class
    return render(request, "home.html", {"apps": items, "form": user_form, "add_class": add_class})

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def test(request):
    return render(request, "test.html")