from django.urls import path
from custom_user import views

urlpatterns = [

    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),


]
