from django.shortcuts import render, redirect
from .models import Task_add as Task_addition
from django.db import transaction
import mysql.connector as m
import json
from django.contrib.auth import logout
# Create your views here.
id=1

@transaction.atomic
def Main_page_one_time_task(request,user):
    global List_of_Tasks
    global id

    Task_head = request.POST.get('Task_heading')
    Task_desc = request.POST.get('Task_description')
    username=user


    Task_add = Task_addition()  
    Task_add.Task_heading = Task_head
    Task_add.Task_description = Task_desc
    Task_add.username=username
    Task_add.Id= id

    sql = f'select * from main_page_task_add where username="{username}";'
    con = m.connect(host='localhost', user='root',password='root', database='ip_project', port='3306')
    cur = con.cursor()
    cur.execute(sql)

    temp =0
    List_of_Tasks = cur.fetchall()
    if Task_head != None or Task_desc!=None:
        for i in range(len(List_of_Tasks)):
            if (Task_head,Task_desc) == List_of_Tasks[i][:2:]:
                temp=1
                break

        if temp==0:
            Task_add.save()
            id+=1



    temp=0




    l = []
    count = 0

    for i in List_of_Tasks:
        if i not in l:
            l += [i]

        count += 1
    

    List_of_Tasks_main = l
    #List_of_Tasks_main=json.dumps(List_of_Tasks_main)

    return render(request, 'Main_page_one_time_task.html', {'List_of_Tasks_main': List_of_Tasks_main, 'List_of_Tasks': List_of_Tasks,'Task_head':Task_head})


def Main_page_daily_task(request):
    return render(request, 'Main_page_daily_task.html')


def delete_task(request,task_id):

    Task_ID=Task_addition.objects.get(Id=task_id)
    Task_ID.delete()
    return redirect('main-page-one-time-task')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')  
    return redirect('login') 





'''Added for commiting purpose'''