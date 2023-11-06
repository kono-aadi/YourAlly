from django.shortcuts import render,redirect



# Create your views here.

from .models import Log_in_datas


def Log_in(request):
    return render(request,"log_in.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        try:
            user_data = Log_in_datas.objects.get(username=username, password=password)
        except Log_in_datas.DoesNotExist:
            return redirect('login')

        
        return redirect('main-page-one-time-task') 

    return render(request, "log_in.html")



        
