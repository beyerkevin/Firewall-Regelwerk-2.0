from django.urls import path
from .import views

urlpatterns = [
    path('', views.header, name='header'),
    path('index/', views.index, name='index'),
    path('ticket/', views.ticket, name='ticket')

]
