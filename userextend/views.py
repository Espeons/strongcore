from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from random import randint

from products.models import SiteUser
from userextend.forms import UserForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = SiteUser
    form_class = UserForm
    success_url = reverse_lazy('login')

    # def form_valid(self, form):
    #     if form.is_valid():
    #         new_user = form.save(commit=False)
    #         new_user.save()
    #         return redirect(self.success_url)
    #     return super().form_valid(form)


