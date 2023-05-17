from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.kk, name='hello'),
    path('book/', views.view_book, name='book'),
]
