from django.contrib import admin
from .models import Hostel

# Register your models here.


class HostelAdmin(admin.ModelAdmin):
    list_display = ['name', 'type']


admin.site.register(Hostel, HostelAdmin)
