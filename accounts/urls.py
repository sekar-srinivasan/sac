from django.urls import path
from .views import SACLoginView, RegistrationView, index_view
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accounts'
urlpatterns = [
    path('', index_view, name='index'),
    # path('register/', views.register_view, name='register'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', SACLoginView.as_view(), {'next': '/donor/'}, name='login'),
    path('logout/', LogoutView.as_view(),{'next': 'accounts:login'}, name='logout'),

]
