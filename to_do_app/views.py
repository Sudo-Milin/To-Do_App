from to_do_app.models import List
from typing import ContextManager
from django.shortcuts import render, redirect

# Create your views here.

def ToDoList(request):
    list_of_task = List.objects.all()
    context =  {
            "list_of_task" : list_of_task
    }
    return render(request, "to_do_app/home.html", context)
