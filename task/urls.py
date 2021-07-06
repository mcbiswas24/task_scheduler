from django.urls import path
from . import views
urlpatterns=[
    
    path('',views.AddTaskPage, name='AddTaskPage'),
    path('showtasks/',views.DisplayTaskPage, name='DisplayTaskPage'),
    path('addtask/',views.AddTask, name='AddTask'),
    path('notify/',views.Notify, name='Notify'),
    path('sendnotification/',views.SendNotification, name='SendNotification'),
    path('logout/',views.Logout, name='Logout')
]