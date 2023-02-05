from django.contrib import admin
from .models import Department, Degree

# Register your models here.

admin.site.register(Degree)


class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'degree']


admin.site.register(Department, DepartmentAdmin)
