from django.urls import path
from . import views

app_name = "to_do_app"

urlpatterns = [
        path("", views.ToDoList, name="List"),
        path("<int:pk>/", views.delete_task, name="delete-task"),
]