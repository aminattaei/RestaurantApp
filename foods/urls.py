from django.urls import path
from .views import food_list,food_detail

app_name='foods'

urlpatterns = [
    path('',food_list,name='food-list'),
    path('<int:pk>/',food_detail,name='detail')
]