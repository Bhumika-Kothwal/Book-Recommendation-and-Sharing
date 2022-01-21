from django.urls import path
from core import views
app_name = 'core'

urlpatterns = [
    path('search_by_name', views.search_by_name, name='search_by_name'),
    path('search_by_genre', views.search_by_genre, name='search_by_genre'),
    path('search_by_author', views.search_by_author, name='search_by_author'),
    path('search_by_similarUser', views.search_by_similarUser, name='search_by_similarUser'),
    path('book_details', views.book_details, name='book_details'),
    path('user_login',views.user_login,name='user_login'),
    path('user_register',views.user_register,name='user_register'),
    #url(r'^base/$', views.base, name='base'),
]