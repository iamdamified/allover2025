from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import ProductsForm

# Create your views here.
# This uses only views.py, settings.py, both urls.py to diplay httpresponse only without templates
def function_name(request):
    return HttpResponse("This is a web app")

# This uses only views.py, settings.py, both urls.py together with templates to display 
def student_page(request):
    students = Student.objects.all()
    return render(request, "Appy/home.html", {"student_list": students})


def productpage(request):
    products = Products.objects.all()
    context = {
        "all_products": products
    }
    return render(request, "Appy/product.html", context)

def singleProductView(request, id):
    single_product = Products.objects.get(id=id)
    context = {
        "product": single_product
    }
    return render(request, "Appy/singleproduct.html", context)

# Format 1
# def formpage(request):
#     products = Products.objects.all()
#     if request.method == "POST":
#         form = ProductsForm(request.POST, request.FILES)#collect data
#         if form.is_valid(): #validate data
#             form.save() # save data
#             return HttpResponse("Your product was successfully created")# then output data
#     else:
#         form = ProductsForm()

#     context = {
#         'product_list': products,
#         'myform': form
#     }
#     return render(request, "Appy/productform.html", context)

# Format 2
def formpage(request):
    if request.method == "GET":
        products = Products.objects.all()
        form = ProductsForm()
        context = {
            'product_list': products,
            'myform': form
        }
        
    elif request.method == "POST":
        form = ProductsForm(request.POST, request.FILES)#collect data
        if form.is_valid(): #validate data
            form.save() # save data    
            return HttpResponse("Your product was successfully created")
        
    return render(request, "Appy/productform.html", context)
        
    