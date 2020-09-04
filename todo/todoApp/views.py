from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import NewUserForm
def index(request):
    tasks = Todo.objects.all().order_by("-added_date")
    return render(request,'todoApp/index.html',{'tasks':tasks})

def add_todo(request):
    current_date = timezone.now()
    content = request.POST["content"]
    discrep = request.POST["disc"]
    username = request.POST['username']
    obj1 = Todo.objects.create(added_date=current_date,text=content,discreption=discrep,active_user=username)
    return HttpResponseRedirect('/')

def done_task(request,task_id):
    Todo.objects.get(id=task_id).delete()
    return HttpResponseRedirect('/')

def login_user(request):
    return render(request,'todoApp/login.html')

def register(request):
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'New Account Created: {username}')
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")
    form = NewUserForm
    return render(request,'todoApp/register.html',{'form':form})

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect("/")

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                  template_name = "todoApp/login.html",
                  context={"form":form})