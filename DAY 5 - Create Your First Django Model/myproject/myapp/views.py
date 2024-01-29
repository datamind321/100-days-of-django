from django.shortcuts import render,HttpResponse
from django.views import View
from .models import Student

# Create your first views here.


# Function Based View

def home(request):
    return HttpResponse("Welcome to Django Tutorial :-)")

def view_data(request):
    data = Student.objects.all()
    return render(request,'myapp/data.html',{'data':data})



# Class Based View 

class Home(View):
    def get(self,request):
        return HttpResponse('Django starts Here :-)')

