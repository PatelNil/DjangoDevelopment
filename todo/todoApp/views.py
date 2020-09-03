from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo

def index(request):
    tasks = Todo.objects.all().order_by("-added_date")
    return render(request,'todoApp/index.html',{'tasks':tasks})

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    obj1 = Todo.objects.create(added_date=current_date,text=content)
    return HttpResponseRedirect('/')

def done_task(request,task_id):
    Todo.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/')