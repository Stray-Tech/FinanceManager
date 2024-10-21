from django.shortcuts import render
from .models import TodoItem, AppItem
from .forms import BillTitle, BillDescription
#from .templatetags.filters import add_class

# Create your views here.
def home(request):
    items = AppItem.objects.all()
    bill_title = BillTitle()
    bill_description = BillDescription()
    #add_class = add_class
    return render(request, "home.html", {
        "apps": items, 
        "bill_form": [bill_title, bill_description]
    })

def todos(request):
    items = TodoItem.objects.all()
    return render(request, "todos.html", {"todos": items})

def test(request):
    return render(request, "test.html")