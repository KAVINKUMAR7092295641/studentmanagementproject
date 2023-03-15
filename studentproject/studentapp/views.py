from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from studentapp.models import Student, City, Course



def log_fun(request):
    return render(request, 'login.html', {'data': ''})



def reg_fun(request):
    return render(request,'registertion.html',{'data':''})


def regdata_fun(request):
    user_name = request.POST['textname']
    user_email = request.POST['tbemail']
    user_password = request.POST['tbpassword']
    print(user_name)

    if User.objects.filter(Q(username=user_name) | Q(email=user_email)| Q(password=user_password)).exists():
        return render(request, 'registertion.html', {'data': 'username,email and password is already exits !!!'})
    else:
        u1 = User.objects.create_superuser(username=user_name, email=user_email, password=user_password)
        u1.save()
        return redirect('log')


def logdata_fun(request):
    user_name = request.POST['textname']
    user_password = request.POST['tbpassword']
    print(user_name,user_password)
    user1 = authenticate(username=user_name, password=user_password)
    print(user1)
    if user1 is not None:
        if user1.is_superuser:
            return redirect('home')
        else:
            return render(request, 'login.html', {'data': 'user is not superuser'})
    else:
        return render(request, 'login.html', {'data': 'enter proper username and password'})


def home(request):

    return render(request, 'home.html')


def addstudent_fun(request):
    city = City.objects.all()
    course = Course.objects.all()
    return render(request,'addstudent.html',{'City_Data':city,'Course_Data':course})


def readdata_fun(request):
        s1 = Student()
        s1.stud_name = request.POST['textname']
        s1.stud_age = request.POST["tbage"]
        s1.stud_phno = request.POST['tbnum']
        s1.stud_city = City.objects.get(City_name=request.POST['ddcity'])
        s1.stud_course = Course.objects.get(course_type=request.POST['ddlcourse'])
        s1.save()
        return redirect('add')

def display_fun(request):
    s1 = Student.objects.all()
    return render(request, 'display.html',{'data':s1})


def update_fun(request,id):
    s1 = Student.objects.get(id=id)
    city = City.objects.all()
    course = Course.objects.all()

    if request.method=='POST':
        s1.stud_name=request.POST['textname']
        s1.stud_age=request.POST['tbage']
        s1.stud_phno=request.POST["tbnum"]
        s1.stud_city=City.objects.get(City_name=request.POST['ddcity'])
        s1.stud_course=Course.objects.get(course_type=request.POST['ddlcourse'])
        s1.save()

        return redirect('display')

    else:
        return render(request,'update.html',{'data':s1,'City_Data':city,'Course_Data':course})


def delete_fun(request,id):
    s1 = Student.objects.get(id=id)
    s1.delete()
    return redirect('display')


def log_out_fun(request):
    return redirect('log')