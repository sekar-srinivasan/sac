from django.urls import path
from django.views.generic import TemplateView
from .views import(
    DonorIndexView,
    DonorCreateView,
    DonorDetailView,
    DonorListView,
    DonorUpdateView,
    DonorDeleteView,
    DonorUserRegistrationView,
    DonationCreateView,
    DonationDetailView,
)

app_name = 'donor'
urlpatterns = [
    path('create-donor-user/', DonorUserRegistrationView.as_view(), name='create-donor-user'),
    path('create/', DonorCreateView.as_view(), name='donor-create'),
    path('<int:pk>/', DonorDetailView.as_view(), name='donor-detail'),
    path('donor-list/', DonorListView.as_view(), name='donor-list'),
    path('', DonorIndexView.as_view(), name='donor-index'),
    # path('donor-home/', DonorTemplateView.as_view(), name='donor-home'),
    path('donation/', DonationCreateView.as_view(), name='donation'),
    path('donation/<int:pk>/', DonationDetailView.as_view(), name='donation-detail'),
    path('<int:pk>/update/', DonorUpdateView.as_view(), name='donor-update'),
    path('<int:pk>/delete/', DonorDeleteView.as_view(), name='donor-delete'),

    # path('asha-searches-child/', TemplateView.as_view(template_name="donor/asha_searches_child.html"), name='asha-searches-child'),

]
