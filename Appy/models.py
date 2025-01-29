from django.db import models
from django import forms
# Importations for Inbuilt User Model Extension.
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



# Inbuilt User Model Extension. Using One to One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)# links a profile data to a User.
    profile_picture = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user}'s profile"


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, **kwargs):
    instance.Profile.save()
# Create your models here.


CATEGORY_CHOICES = (
    ('E', 'Electronics'),
    ('F', 'Fashion'),
    ('B', 'Baby'),
    ('W', 'Women'),
    ('M', 'Men')
)

class Products(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    image = models.ImageField(upload_to="product_images", default="product.jpg")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Products'


class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mat_number = models.BigIntegerField()
    dept = models.TextField()


def __str__ (self):
    return self.mat_number


# Regular/Basic Form for Student which can be placed in any file.
class StudentForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField(label="your email")
    mat_number = forms.IntegerField()
    dept = forms.CharField(max_length=50)