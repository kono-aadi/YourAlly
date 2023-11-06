from django.shortcuts import render,redirect
from .models import sign_up_datas
from Log_in_page.models import Log_in_datas
from django.db import IntegrityError
# Create your views here.




def sign_up(request):
    return render(request,'sign_up.html')


def register(request):
    if request.method=='POST':
        Fname=request.POST.get('first_name')
        Lname=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        Password=request.POST.get('password')
        try:
            user_data = sign_up_datas(first_name=Fname, last_name=Lname, email=email, username=username, password=Password)
            user_data.save()
            login_data = Log_in_datas(username=username, password=Password)
            login_data.save()
            return redirect('login')
        except IntegrityError:
            errormsg = "Username or email already exists. Please choose a different one."
            return render(request, 'sign_up.html', {'error_message': errormsg})
    


    return render(request, 'sign_up.html')





    

    

     

