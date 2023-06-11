from django.urls import path
from . import views

urlpatterns = [
    path('', views.Registration.as_view(), name='registration'),
    path("login/", views.EnterLoginView.as_view(), name="login"),
    path("users/", views.UserListView.as_view(), name="user_list"),
]
