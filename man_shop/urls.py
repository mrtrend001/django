from django.urls import path
from . import views
from user.views import Registration


urlpatterns = [
    path('cloth', views.cloth_view, name='clothes'),
    path('cloth_detail/<int:id>/', views.cloth_detail_view, name='cloth_detail'),
    path('cloth_detail/<int:id>/delete/', views.delete_cloth_view, name='cloth_delete'),
    path('cloth_detail/<int:id>/update/', views.update_cloth_view, name='cloth_update'),
    path('add-cloth/', views.create_cloth_view, name='create_cloth'),
]



