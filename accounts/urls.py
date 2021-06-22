from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'^login/$', auth_views.LoginView.as_view(), {'title': 'Вход'}, name='login'),
    path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    path(r'^signup/$', views.RegisterUser.as_view(), {'title': 'Регистрация'}, name='signup'),
    path(r'^$', views.dashboard, name='Profile'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
