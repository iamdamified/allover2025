from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', function_name),
    path('students/', student_page),
    path("product/", productpage, name="product"),
    path("<int:id>/", singleProductView, name="singleproduct"),
    path("prodform/", formpage, name="prodform"),
    path("studentform/", regformpage, name="regform")
]