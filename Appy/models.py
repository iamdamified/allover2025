from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mat_number = models.BigIntegerField()
    dept = models.TextField()


def __str__ (self):
    return self.mat_number



CATEGORY_CHOICES = (
    ('E', 'Electronics'),
    ('F', 'Fashion'),
    ('B', 'Baby'),
    ('W', 'Women'),
    ('M', 'Men')
)

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    image = models.ImageField(upload_to="product_images", default="product.jpg")

    def __str__(self):
        return self.name

