from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.http import HttpResponse
from .models import *
from authentication.models import User_Table
from datetime import date
from datetime import datetime
import calendar
from .tasks import sendMail

# Create your views here.

def AddTaskPage(request):
    return render(request,"task/AddTask.html")

def DisplayTaskPage(request):
    task_dets = Task_Details.objects.filter(Email = request.session['email'])
    dates = Task_Details.objects.values('StartDate','Day').filter(Email = request.session['email']).order_by('StartDate').distinct()
    p1 = Task_Details.objects.filter(Priority = 1).count()
    p2 = Task_Details.objects.filter(Priority = 2).count()
    p3 = Task_Details.objects.filter(Priority = 3).count()
    p4 = Task_Details.objects.filter(Priority = 4).count()
    p5 = Task_Details.objects.filter(Priority = 5).count()
    
    return render(request,"task/DisplayTask.html",{'tasks':task_dets,'dates':dates,'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5})

def Notify(request):
    return render(request,"task/NotifyPage.html")

def AddTask(request):
    email = User_Table.objects.get(Email = request.session['email'])
    task_name = request.POST['taskname']
    task_desc = request.POST['taskdescription']
    priority = request.POST['radiocheck']
    start_date = request.POST['startdate']
    end_date = request.POST['deadline']

    #getting the day
    year,month,day = start_date.split("-")
    dt = date(int(year),int(month),int(day))
    day = calendar.day_name[dt.weekday()]

    try:
        new_task = Task_Details.objects.create(
            Email = email,
            TaskName = task_name,
            TaskDescription = task_desc,
            Priority = priority,
            StartDate = start_date,
            EndDate = end_date,
            Day = day
        )
        message = "Your task has been added. Go to Display Schedule to see your tasks"
        return render(request,"task/AddTask.html",{'message':message})
    except BaseException:
        message = "Sorry, could not add your task. Please try again"
        return render(request,"task/AddTask.html",{'message':message})


def SendNotification(request):
    email = request.POST['email']
    event_name = request.POST['ename']
    date =  request.POST['date'] 
    time =  request.POST['time']

    message = 'An Email will be sent on {} to remind you for the event {}'.format(date,event_name)
    email_body = "Reminding you for the event '{}'".format(event_name)

    #Calculating seconds 
    curr_date = datetime.now()

    hour,minute = time.split(":") #spliting time into hours and minutes
    year,month,day = date.split("-") #spliting date into year month and day

    #getting the future date and time
    future_date = datetime(int(year),int(month),int(day),int(hour),int(minute),0)

    #getting total no of seconds between current and given future date and time
    seconds = round((future_date-curr_date).total_seconds())

    if seconds < 0:
        message = "Please enter future date and time"
        return render(request,'task/NotifyPage.html',{'message':message})
    else:
        #calling the celery task with given parameters
        sendMail.delay(seconds,email,email_body)
        return render(request,'task/NotifyPage.html',{'message':message})

def Logout(request):
    del request.session['email']
    del request.session['password']

    return redirect('/authentication/')