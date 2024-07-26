from django.contrib import admin
from django.urls import path
from . import views


app_name='todo'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
    path('create/',views.CreateView.as_view(),name='create'),
    
]