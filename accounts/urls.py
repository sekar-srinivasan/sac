from django.urls import path
from .views import SACLoginView, RegistrationView, index_view
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    )

app_name = 'accounts'
urlpatterns = [
    path('', index_view, name='index'),
    # path('register/', views.register_view, name='register'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', SACLoginView.as_view(), {'next': '/donor/'}, name='login'),
    path('logout/', LogoutView.as_view(),{'next': 'accounts:login'}, name='logout'),
    path('change-password/', PasswordChangeView.as_view(template_name='registration/change_password.html', success_url='/sac/'), name='change-password'),
    path('reset-password/', PasswordResetView.as_view(template_name='registration/reset_password.html'), name='reset-password'),

]
