from django.urls import path
from .views import *

urlpatterns = [
    path('hostel/', HostelList.as_view()),
    path('hostel/<pk>', HostelDetail.as_view()),
]
