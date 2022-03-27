from django.shortcuts import render, redirect
from .models import Task, User

from .forms import TodoForm, CustomUserCreationForm, SortingForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def loginUser(requset):
    page = 'login'

    if requset.user.is_authenticated:
        return redirect('todos')

    if requset.method == 'POST':
        email = requset.POST['email']
        password = requset.POST['password']

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(requset, 'Username does not exist')

        user = authenticate(requset, email=email, password=password)

        if user is not None:
            login(requset, user)
            return redirect('todos')
        else:
            messages.error(requset,"Email OR Password is incorrect")
    
    return render(requset, 'base/login_register.jinja')


def logoutUser(request):
    logout(request)
    messages.info(request, 'User was logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            form.save()
            messages.success(request, "User account was created")
            login(request, user)
            return redirect('todos')
        else:
            messages.error(request, "Error has occured")
        
    context = {'page':page, 'form':form}
    return render(request, 'base/login_register.jinja', context)
        


@login_required(login_url='login')
def todoList(request):
    user = request.user
    todos = Task.objects.filter(user=user)
    choice = SortingForm(request.POST or None)
    if request.method == 'POST':
        if choice.is_valid():
            temp = choice.cleaned_data.get("sort_by")
            todos = Task.objects.filter(user=user).order_by(temp)
    
    context = {'todos':todos, 'choices':choice}
    return render(request, 'base/todos.jinja', context)


@login_required(login_url='login')
def todoCreate(request):
    user = request.user
    form = TodoForm()
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = user
            todo.save()
            messages.success(request, "Todo was added successfully!")
            return redirect('todos')
    
    context = {'form': form}
    return render(request, 'base/todo_form.jinja', context)


@login_required(login_url='login')
def todoUpdate(request, pk):
    todo = Task.objects.get(id=pk)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo was Updated successfully!")
            return redirect('todos')

    context = {'form': form}
    return render(request, 'base/todo_form.jinja', context)


@login_required(login_url='login')    
def todoDelete(request, pk):
    todo = Task.objects.get(id=pk)
    if request.method == 'POST':
        todo.delete()
        messages.success(request, "Todo was Deleted successfully!")
        return redirect('todos')
    context = {'todo':todo}
    return render(request, 'base/delete.jinja', context)
    







