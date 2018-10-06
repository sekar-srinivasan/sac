from django.urls import path
from .views import(
    DonorCreateView,
    DonorDetailView,
    DonorListView,
    DonorUpdateView,
    DonorDeleteView,
    DonorUserRegistrationView,
    DonationView,
)

app_name = 'donor'
urlpatterns = [
    path('create-donor-user/', DonorUserRegistrationView.as_view(), name='create-donor-user'),
    path('create/', DonorCreateView.as_view(), name='donor-create'),
    path('<int:pk>/', DonorDetailView.as_view(), name='donor-detail'),
    path('', DonorListView.as_view(), name='donor-list'),
    path('donation/', DonationView.as_view(), name='donation'),
    path('<int:pk>/update/', DonorUpdateView.as_view(), name='donor-update'),
    path('<int:pk>/delete/', DonorDeleteView.as_view(), name='donor-delete'),
]
