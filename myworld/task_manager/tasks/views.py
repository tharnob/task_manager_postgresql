from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Task
from django.views.decorators.csrf import csrf_protect

# Create your views here.

def home(request):
    task = Task.objects.all().values()
    template = loader.get_template('home.html')
    context = {
        "task": task,
    }
    return HttpResponse(template.render(context, request))

@csrf_protect
def add_task(request):
    if request.method == 'POST':
        print("Added")

        #retreive the user inputs
        task_title = request.POST.get("title")
        task_description = request.POST.get("description")
        task_due_date = request.POST.get("due_date")
        task_priority = request.POST.get("priority")
    

        #create an object for models
        s = Task()
        s.title=task_title
        s.description=task_description
        s.due_date=task_due_date
        s.priority=task_priority
        

        s.save()
        return redirect("/tasks")


    template = loader.get_template("add_task.html")
    context = {'some_key': 'some_value'}
    return HttpResponse(template.render(context, request))




def delete_task(request, id):
    s = Task.objects.get(pk=id)
    s.delete()

    return redirect("/tasks")


def update_task(request, id):
    s = Task.objects.get(pk=id)

    template = loader.get_template("update_task.html")
    context = {'task': s}
    return HttpResponse(template.render(context, request))


def do_update_task(request, id):
    task_title = request.POST.get("title")
    task_description = request.POST.get("description")
    task_due_date = request.POST.get("due_date")
    task_priority = request.POST.get("priority")


    s = Task.objects.get(pk=id)
    s.title=task_title
    s.description=task_description
    s.due_date=task_due_date
    s.priority=task_priority

    s.save()
    return redirect("/tasks")
