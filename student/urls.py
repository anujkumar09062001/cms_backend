from django.urls import path
from .views import *

urlpatterns = [
    path('student/', StudentList.as_view()),
    path('student/<pk>', StudentDetail.as_view())
]
