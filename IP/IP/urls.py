"""
URL configuration for IP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Log_in_page import views as log_in_view
from sign_up_page import views as sign_up_view
from index_page import views as index_view
from Main_page import views as main_view


urlpatterns = [
    path('admin/'               ,    admin.site.urls                          ),
    path('loginpage'            ,    log_in_view.login , name='login'                      ),
    path('indexpage'            ,    index_view.index                , name='indexpage'         ),
    path(''            ,    index_view.index                , name='indexpage'         ),
    path('signuppage'           ,    sign_up_view.register , name='register'                    ),
    path('mainpageonetimetask/<str:user>'  ,    main_view.Main_page_one_time_task,name='main-page-one-time-task'),
    path('delete_task/<int:task_id>',    main_view.delete_task, name='delete-task'),
    path('logout/', main_view.logout_view, name='logout'),


]