from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from .models import *
from .util import *
import random

# Create your views here.

def MainPage(request):
    return render(request,'authentication/MainPage.html')
    
def LoginPage(request):
    return render(request,'authentication/LoginPage.html')

def RegistrationPage(request):
    return render(request,'authentication/RegistrationPage.html')

def Registration(request):
    try:
        first_name = request.POST['fname'] 
        last_name = request.POST['lname'] 
        email = request.POST['email'] 
        password = request.POST['pwd'] 
        r_password = request.POST['r_pwd'] 

        user = User_Table.objects.filter(Email=email)

        if user:
            message = 'This email already exists'
            return render(request, 'authentication/RegistrationPage.html', {'message':message})
        else:
            if password == r_password:
                new_user = User_Table.objects.create(FirstName = first_name,  LastName = last_name, Email = email, Password = password)
                message = 'Registration successful'
                return render(request, 'authentication/LoginPage.html', {'message': message})
            else:
                message = 'Password and confirm password does not match'
                return render(request, 'authentication/RegistrationPage.html', {'message': message})
    except User_Table.DoesNotExist:
        message = 'This email already exists'
        return render(request, 'authentication/RegistrationPage.html', {'message': message}) 

def Login(request):
    try:
        email = request.POST['email']
        password = request.POST['pwd']

        user = User_Table.objects.get(Email=email)

        if user.Password == password:
            request.session['email'] = email
            request.session['password'] = password
            return redirect('/task/') 
        else:
            message = "Incorrect password or email"
            return render(request,  'authentication/LoginPage.html', {'message':message})
    except User_Table.DoesNotExist:
        message = "Email does not exists"
        return render(request, 'authentication/LoginPage.html', {'message': message}) 

def ChangePassword(request):
    email = request.POST['em']
    password = request.POST['pwd']
    c_password = request.POST['repwd']
    try:
        edit_user = User_Table.objects.get(Email=email)

        if password == c_password:
            otp = random.randint(100000,999999)
            sendmail('Password Change','login_template',email,{'name':edit_user.FirstName,'otp':otp})
            return render(request, 'authentication/OtpPage.html',{'email':email,'otp':otp,'password':password})
        else:
            message = "Entered password and retyped passsword does not match"
            return (request,'authentication/ForgotPassword.html',{'message':message})
    except BaseException:
        message = "Email does not exists"
        return (request,'authentication/ForgotPassword.html',{'message':message})

       
def ForgotPassword(request):
    return render(request, 'authentication/ForgotPassword.html')

def OTPVerification(request,email,otp,password):
    entered_otp = request.POST['eotp']
    edituser = User_Table.objects.get(Email=email)
    if int(entered_otp) == otp:
        edituser.Password = password
        edituser.save()
        message = 'your password has been successfully changed'
        return render(request,'authentication/LoginPage.html',{'message':message})
    else:
        message = 'Wrong OTP entered. New OTP has been sent to your mail'
        sendmail('Password Change','login_template',email,{'name':edituser.FirstName,'otp':otp})
        return render(request, 'authentication/OtpPage.html',{'email':email,'otp':otp,'password':password})