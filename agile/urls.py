from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.routers')),
    path('', lambda req: HttpResponse("Welcome to my site!"))

]
