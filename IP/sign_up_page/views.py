from django.shortcuts import render
from .models import sign_up_datas
# Create your views here.




def sign_up(requet):
    return render(requet,'sign_up.html')


def dummy1(request):
    Fname=request.POST['first_name']
    Lname=request.POST['last_name']
    email=request.POST['email']
    username=request.POST['username']
    Password=request.POST['password']
    
    Datas=sign_up_datas()
    Datas.first_name=Fname
    Datas.last_name=Lname
    Datas.email=email
    Datas.username=username
    Datas.password=Password
    Datas.save()

    return render(request,"dummy.html")

