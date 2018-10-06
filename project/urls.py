from django.urls import path
from .views import(
    ProjectCreateView,
    ProjectDetailView,
    ProjectListView,
    ProjectUpdateView,
    ProjectDeleteView,
    PartnerUserRegistrationView,
)

app_name = 'project'
urlpatterns = [
    path('create-partner-user/', PartnerUserRegistrationView.as_view(), name='create-partner-user'),
    path('create/', ProjectCreateView.as_view(), name='project-create'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/update/', ProjectUpdateView.as_view(), name='project-update'),
    path('<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
]
