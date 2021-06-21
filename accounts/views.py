from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView



@login_required
def dashboard(request):
    return render(request, 'accounts/Profile.html', {'title': 'Profile'})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()))


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
