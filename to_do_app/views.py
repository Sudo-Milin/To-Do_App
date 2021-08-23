from django.shortcuts import render, redirect
from . models import List
from . forms import ListModelForm
# Create your views here.

def ToDoList(request):
    list_of_task = List.objects.all().order_by("-date_added")
    form = ListModelForm()
    if request.method == "POST":
        form = ListModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/")

    context =  {
            "list_of_task" : list_of_task,
            "form": form
    }
    return render(request, "to_do_app/home.html", context)

def delete_task(request, pk):
        task = List.objects.get(id=pk)
        task.delete()
        return redirect("/")


