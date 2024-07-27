from django.contrib import admin
from django.urls import path
from . import views


app_name='todo'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>',views.DetailView.as_view(),name='detail'),
    path('create/',views.CreateView.as_view(),name='create'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),
    path('signup/',views.signupview,name='signup'),
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    
]
