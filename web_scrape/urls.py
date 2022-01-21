from django.contrib import admin
from django.urls import path
from web_scrape import views


app_name='web_scrape'

urlpatterns = [
     path('webscrape', views.webscrape, name='webscrape'),
]
