from django.urls import path
from .views import(
    DonorCreateView,
    DonorDetailView,
    DonorListView,
    DonorUpdateView,
    DonorDeleteView,
)

app_name = 'donor'
urlpatterns = [
    path('create/', DonorCreateView.as_view(), name='donor-create'),
    path('<int:pk>/', DonorDetailView.as_view(), name='donor-detail'),
    path('', DonorListView.as_view(), name='donor-list'),
    path('<int:pk>/update/', DonorUpdateView.as_view(), name='donor-update'),
    path('<int:pk>/delete/', DonorDeleteView.as_view(), name='donor-delete'),
]
