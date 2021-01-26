from django.urls import path
from . import views

app_name= 'main_app'

urlpatterns = [
    path('forms/', views.get_form, name='forms'),
    path('', views.index, name='index'),
    path('tables/', views.tables, name='tables'),
    path('register/',views.register, name='register'),
    path('user_login/',views.user_login,name='user_login'),
    path('logout/', views.user_logout, name='logout'),
    path('graph/',views.graph,name='graph'),
]