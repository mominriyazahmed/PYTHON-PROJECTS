from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
# Create your views here.
def home(request):
    return render(request, 'home.html')

def stu(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        try:
            if form.is_valid():
                form.save()
                return redirect('/show')
        except:
            pass
    else:
        form = StudentForm()
    return render(request, 'index.html',{'form':form})

def show(request):
    students = Student.objects.order_by('name')
    return render(request, 'show.html',{'students':students})

def edit(request, rollno):
    student = Student.objects.get(rollno=rollno)
    return render(request, 'edit.html',{'student':student})

def update(request, rollno):
    student = Student.objects.get(rollno=rollno)
    form = StudentForm(request.POST,instance=student)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request, 'edit.html',{'student':student})

def delete(request, rollno):
    student = Student.objects.get(rollno=rollno)
    student.delete()
    return redirect('/show')