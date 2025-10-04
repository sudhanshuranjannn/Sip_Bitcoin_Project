from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Bitcoin SIP API 🚀"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('api/auth/', include('sipapp.urls')),
]
