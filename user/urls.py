from django.urls import path
from .views import *

urlpatterns = [
    path('current_user/', Current_User),
]
