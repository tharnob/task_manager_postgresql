from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('tasks/', views.home, name='tasks'),
    path("add_task/", views.add_task, name="add_task"),
    path("delete-task/<int:id>", views.delete_task, name="delete_task"),
    path("update-task/<int:id>", views.update_task, name="update_task"),
    path("do-update-task/<int:id>", views.do_update_task, name="do_update_task"),

]