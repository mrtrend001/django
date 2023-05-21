from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.kk, name='hello'),
    path('', views.view_book, name='book'),
]
