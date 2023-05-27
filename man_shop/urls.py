from django.urls import path
from . import views


urlpatterns = [
    path('', views.cloth_view, name='clothes'),
    path('cloth_detail/<int:id>/', views.cloth_detail_view, name='cloth_detail'),
    path('add-cloth/', views.create_cloth_view, name='create_cloth'),
]
