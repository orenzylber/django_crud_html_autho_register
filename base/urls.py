from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('index/', views.index),
    path('students/<int:id>',views.MyStudentsView.as_view()),
    path('students/',views.MyStudentsView.as_view()), 
]
