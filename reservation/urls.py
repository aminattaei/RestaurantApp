from django.urls import path,include
from .views import reserve


app_name='reservation'

urlpatterns = [
    path('',reserve,name='book')
]