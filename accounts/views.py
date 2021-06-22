from django.shortcuts import render
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView



@login_required
def dashboard(request):
    return render(request, 'accounts/Profile.html', {'title': 'Профиль'})


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))


def request(request):
    return {'request': request}
