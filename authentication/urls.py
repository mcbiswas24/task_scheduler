from django.urls import path
from . import views
urlpatterns=[

     path('',views.MainPage, name='MainPage'),
    path('loginpage', views.LoginPage, name='LoginPage'),
    path('Registration/', views.RegistrationPage, name='RegistrationPage'),
    path('register/', views.Registration, name='Registration'),
    path('login/',views.Login, name='Login'),
    path('forgotpassword/',views.ForgotPassword, name='ForgotPassword'),
    path('changepassword/',views.ChangePassword, name='ChangePassword'),
    path('otpvalidate/<str:email>/<int:otp>/<str:password>',views.OTPVerification, name='OTPVerification'),
]