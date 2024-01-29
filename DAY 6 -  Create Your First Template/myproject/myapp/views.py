from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from django.views import View
from .models import Student
from .forms import StudentForm
from django.contrib import messages

# Create your first views here.


# Function Based View

def home(request):
    return HttpResponse("Welcome to Django Tutorial :-)")

def view_data(request):
    data = Student.objects.all().order_by('name')
    return render(request,'myapp/data.html',{'data':data})


def create_data(request):
    fm = StudentForm()
    if request.method=='POST':
        fm = StudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/data/')

            
            
    return render(request,'myapp/form.html',{'form':fm})

def update_data(request,id):
    fm = StudentForm()
    obj = Student.objects.get(id=id)
    if request.method=='POST':
        fm = StudentForm(request.POST,instance=obj)
        if fm.is_valid():
            
            fm.save()

            return HttpResponseRedirect('/data/')
    else:
        fm = StudentForm(instance=obj)
        
    return render(request,'myapp/form-update.html',{'form':fm})

def delete_data(request,id):
    obj = Student.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/data/')


# Class Based View 

class Home(View):
    def get(self,request):
        return HttpResponse('Django starts Here :-)')

