from django.shortcuts import render

# Create your views here.

from .models import Log_in_datas


def Log_in(request):
    return render(request,"log_in.html")

def dummy2(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        

        datas=Log_in_datas()
        datas.username=username
        datas.password=password
        datas.save()

    return render(request,'dummy.html')