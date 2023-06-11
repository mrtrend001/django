from django.shortcuts import render
from django.contrib.auth.forms import User, UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.views.generic import CreateView, ListView


class Registration(CreateView):
    form_class = UserCreationForm
    success_url = 'users/'
    template_name = "user/registration.html"


class EnterLoginView(LoginView):
    form_class = AuthenticationForm
    template_name = "user/login.html"

    def get_success_url(self):
        return reverse("user:user_list")


class UserListView(ListView):
    queryset = User.objects.all()
    template_name = "user/user_list.html"




