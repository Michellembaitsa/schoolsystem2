from django.shortcuts import render
from student.models import Student


# Create your views here.

def home(request):
    students=Student.objects.count()
    data={"students":students}

    return render(request,"home.html",data)

def video(request):
    obj=Item.objects.all()
    return render(request,'home.html',{'obj':obj})

def dashboard(request):
    students=Student.objects.count()
    data={"students":students}
    return render(request,'dashboard.html',data)


