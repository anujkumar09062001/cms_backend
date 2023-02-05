from django.urls import path
from .views import *

urlpatterns = [
    path('degree/', DegreeList.as_view()),
    path('degree/<pk>', DegreeDetail.as_view()),
    path('department/', DepartmentList.as_view()),
    path('department/<pk>', DepartmentDetail.as_view()),
]
