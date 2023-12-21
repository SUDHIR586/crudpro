from django.shortcuts import render,redirect
from testapp.forms import EmployeeForm
from testapp.models import Employee
# Create your views here.

# employees entry
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'testapp/index.html',{'form':form})

# all employees show
def show(request):
    employees = Employee.objects.all()
    return render(request,'testapp/show.html',{'employees':employees})

# employee edit
def edit(request,id):
    employee = Employee.objects.get(id=id)
    return render(request,'testapp/edit.html',{'employee':employee})

# employee update
def update(request,id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST,instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/show')
    return render(request,'testapp/edit.html',{'employee':employee})

# employee delete
def delete(request,id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')
