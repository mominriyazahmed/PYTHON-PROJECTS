from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task
# Create your views here.
def home(request):
    return render(request, 'home.html')

def task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except:
            pass
    else:
        form = TaskForm()
    return render(request, 'index.html',{'form':form})

def show(request):
    tasks = Task.objects.order_by('time')
    return render(request, 'show.html',{'tasks':tasks})

def edit(request, tid):
    task = Task.objects.get(tid=tid)
    return render(request, 'edit.html',{'task':task})

def update(request, tid):
    task = Task.objects.get(tid=tid)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html', {'task':task})

def delete(request, tid):
    task = Task.objects.get(tid=tid)
    task.delete()
    return redirect('/show')