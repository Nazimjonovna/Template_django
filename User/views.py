from django.shortcuts import render
from django.views.generic import CreateView
from .forms import UserForm
from .models import UserData

# Create your views here.
class UserView(CreateView):
    model = UserData
    form_class = UserForm
    template_name = 'user.html'
    success_url = 'endi_otp'
