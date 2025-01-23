
from django.contrib import admin
from django.urls import path,include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
   
] 

admin.site.site_header = "Student management"
admin.site.site_title = "Student management Portal"
admin.site.index_title = "Welcome to Student management Portal"