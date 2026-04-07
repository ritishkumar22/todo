from django.shortcuts import render, redirect
from .models import Todo
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

@login_required(login_url='login')
def todo_list(request):
    search_input = request.GET.get('search-area') or ''
    if search_input:
        todos = Todo.objects.filter(user=request.user, title__icontains=search_input)
    else:
        todos = Todo.objects.filter(user=request.user)

    if request.method == 'POST':
        if 'add_task' in request.POST:
            new_title = request.POST.get('title')
            if new_title:
                Todo.objects.create(user=request.user, title=new_title)
        
        elif 'delete_task' in request.POST:
            task_id = request.POST.get('task_id')
            Todo.objects.get(id=task_id).delete()
        
        elif 'complete_task' in request.POST:
            task_id = request.POST.get('task_id')
            task = Todo.objects.get(id=task_id)
            task.completed = not task.completed
            task.save()
            
        return redirect('/')

    return render(request, 'todo/list.html', {'todos': todos, 'search_input': search_input})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'todo/signup.html', {'form': form})

