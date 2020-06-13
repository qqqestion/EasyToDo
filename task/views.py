from django.shortcuts import render, redirect, get_object_or_404

from .models import *
from .forms import TaskForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        form.instance.author = request.user
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        tasks = Task.objects.all().order_by('-date')
        form = TaskForm()
        context = {
            'tasks': tasks,
            'form': form,
        }
    return render(request, 'task/task_list.html', context)

def complete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect(home)
