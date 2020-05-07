from django.urls import path
from django.conf import settings
from . import views


urlpatterns = [
    path('',views.all_blogs, name = 'all_blogs'),
    
]