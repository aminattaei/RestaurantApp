from django.urls import path
from .views import BlogList


urlpatterns = [
    path('',BlogList,name='blog-list')
]
