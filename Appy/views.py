from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Product

# Create your views here.
# This uses only views.py, settings.py, both urls.py to diplay httpresponse only without templates
def function_name(request):
    return HttpResponse("This is a web app")

# This uses only views.py, settings.py, both urls.py together with templates to display 
def student_page(request):
    students = Student.objects.all()
    return render(request, "Appy/home.html", {"student_list": students})


def productpage(request):
    products = Product.objects.all()
    context = {
        "all_products": products
    }
    return render(request, "Appy/product.html", context)

def singleProductView(request, id):
    single_product = Product.objects.get(id=id)
    context = {
        "product": single_product
    }
    return render(request, "Appy/singleproduct.html", context)