from django.shortcuts import render
from .models import Student

# Create your views here.

def view_data(request):
    data = Student.objects.all()
    return render(request,'myapp/data.html',{'data':data})
