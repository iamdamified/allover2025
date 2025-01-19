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




# Regular/Base Form: form can be defined in any file and called from it.
def regformpage(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid(): #Below this valid we cannot use save, but cleaned data format
            student_name = form.cleaned_data["name"]
            student_email = form.cleaned_data["email"]
            student_mat_number = form.cleaned_data["mat_number"]
            student_dept = form.cleaned_data["dept"]

            Student.objects.create(name=student_name, email=student_email, mat_number=student_mat_number, dept=student_dept)
            return HttpResponse("Thank you")
        
    else:
        form = StudentForm(request.POST)
    context = {
        "Sform": form
    }
    return render(request, "Appy/Regularform.html", context)



# Format 1 Model Form and with Initialization of values.
def formpage(request):
    products = Products.objects.all()
    if request.method == "POST":
        form = ProductsForm(request.POST, request.FILES)#collect data
        if form.is_valid(): #validate data
            form.save() # save data
            return HttpResponse("Your product was successfully created")# then output data
    else:
        form = ProductsForm(initial={"name":"Your Name", "description":"short explanation", "price":"0.00","category":"select", "image":"upload"})

    context = {
        'product_list': products,
        'myform': form
    }
    return render(request, "Appy/productform.html", context)

# Format 2 Model Form and without initializing values.
# def formpage(request):
#     if request.method == "GET":
#         products = Products.objects.all()
#         form = ProductsForm()
#         context = {
#             'product_list': products,
#             'myform': form
#         }
        
#     elif request.method == "POST":
#         form = ProductsForm(request.POST, request.FILES)#collect data
#         if form.is_valid(): #validate data
#             form.save() # save data    
#             return HttpResponse("Your product was successfully created")
        
#     return render(request, "Appy/productform.html", context)



# Multiple data objects outputs on same page, including a form altogether.
# def home_page(request):

#     if request.method == "GET":
#         all_categories = Category.objects.all()
#         # mens_products = Product.objects.filter(category=2) # A foreignKey called in model for category uses id and not the English name given to the choices as done in Category class
#         mens_products = Product.objects.filter(category__name="MEN") # This helps the database to recognize and use the Instance name and not its default ID
#         womens_products = Product.objects.filter(category__name="WOMEN")
#         kids_products = Product.objects.filter(category__name="kids")
#         social_images = Social.objects.all()

#         context = {
#             'all_categories': all_categories,
#             'mens_product': mens_products,
#             'womens_product': womens_products,
#             'kids_product': kids_products,
#             'social_images': social_images

#         }

#     # Bound instance, this is used to receive entries from a frontend built form into the backend.
#     elif request.method == "POST":
#         #  NOTE The name and email we have in the bracket in quotes is pointing to the name and email in quote in the form
#         new_subscribers_name = request.POST["name"] # OR request.POST.get("name")
#         new_subscribers_email = request.POST("email") # OR request.POST.get["email"]
#         # The below is the ORM that describes what operation the application does with the data received from the user throught the form.
#         Subscriber.objects.create(name=new_subscribers_name, email=new_subscribers_email)
#         # The below describes what the form reaction would be after submiting
#         # return HttpResponse("You have subscribed sucessfully")
#         return redirect("productslink")
    
#     return render(request, "myapp/index.html", context)


# # Learn more about SENDGRID on twilo.com to know how to distribute newsletters to emails collected from this form (twilo.com/blog/email-activation-django-sendgrid)
