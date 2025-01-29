from django.contrib import admin
from .models import Products, Student, Profile

# Register your models here.


admin.site.register(Products)
# admin.site.register(Student)




class StudentAdmin(admin.ModelAdmin):
    list_display = ["name","mat_number", "email"]
    list_filter = ["dept"]
    list_editable = ["email"]

admin.site.register(Student, StudentAdmin)


admin.site.register(Profile)