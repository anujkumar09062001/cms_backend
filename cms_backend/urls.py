from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apiV1/token-auth/', obtain_jwt_token),
    path('apiV1/', include('administration.urls')),
    path('apiV1/', include('hostel.urls')),
    path('apiV1/', include('student.urls')),
    path('apiV1/', include('user.urls')),
]
