from django.contrib import admin
from django.urls import path
from donation import views


app_name='donation'

urlpatterns = [
     #path('', views.index, name='index'),
     path('nearby/', views.nearby, name='nearby'),
     path('map_near_ngo/', views.map_near_ngo, name='map_near_ngo'),
     path('ngo_form/', views.ngo_form, name='ngo_form'),
]
