from django.contrib import admin
from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('home/', function_name),
    path('students/', student_page),
    path("product/", productpage, name="product"),
    path("<int:id>/", singleProductView, name="singleproduct"),
    path("prodform/", formpage, name="prodform"),
    path("studentform/", regformpage, name="regform"),
    path("useregform/", useregistration, name="usereg"),
    path("customuserregform/", customfrontendusereg, name="customusereg"),
    path("login/", LoginView.as_view(template_name="Appy/login.html"), name="login"),
    path("logout/", LogoutView.as_view(template_name="Appy/logout.html"), name="logout"),
    path("frontlogin/", frontend_login, name="frontlogin"),
    path("frontlogout/", frontend_logout, name="frontlogout")
]