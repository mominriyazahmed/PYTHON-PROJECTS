from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def home(request):
  return render(request, 'home.html')

def emp(request):
  if request.method == 'POST':
    form = EmployeeForm(request.POST)
    try:
         if form.is_valid():
          form.save()
          return redirect('/show')
    except:
        pass
  else:
      form = EmployeeForm()
  return render(request,'index.html',{'form':form})
  
def show(request):
  employees = Employee.objects.order_by('Ename')
  return render(request,'show.html',{ 'employees' : employees })

def edit(reuest,Eid):
  employee=Employee.objects.get(Eid=Eid)
  return render(reuest,'edit.html',{"employee":employee})

def update(request,Eid):
  employee = Employee.objects.get(Eid=Eid)
  form  = EmployeeForm(request.POST,instance=employee)
  if form.is_valid():
    form.save()
    return redirect('/show')
  return render(request,'edit.html',{"employee":employee})

def delete(request,Eid):
  employee = Employee.objects.get(Eid=Eid)
  employee.delete()
  return redirect("/show")

