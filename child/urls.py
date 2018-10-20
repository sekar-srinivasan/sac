from django.urls import path
from .views import(
    ChildCreateView,
    ChildDetailView,
    ChildListView,
    ChildUpdateView,
    ChildDeleteView,

    ProgressCreateView,
    ProgressListView,
    ProgressDetailView,
    ProgressUpdateView,
    ProgressDeleteView,
)

app_name = 'child'
urlpatterns = [
    path('create/<int:project_pk>', ChildCreateView.as_view(), name='child-create'),
    path('<int:pk>/', ChildDetailView.as_view(), name='child-detail'),
    path('', ChildListView.as_view(), name='child-list'),
    path('<int:pk>/update/', ChildUpdateView.as_view(), name='child-update'),
    path('<int:pk>/delete/', ChildDeleteView.as_view(), name='child-delete'),

    path('<int:child_pk>/progress/create/', ProgressCreateView.as_view(), name='progress-create'),
    path('<int:child_pk>/progress/<int:pk>/', ProgressDetailView.as_view(), name='progress-detail'),
    path('<int:child_pk>/progress/', ProgressListView.as_view(), name='progress-list'),
    path('<int:child_pk>/progress/<int:pk>/update/', ProgressUpdateView.as_view(), name='progress-update'),
    path('<int:child_pk>/progress/<int:pk>/delete/', ProgressDeleteView.as_view(), name='progress-delete'),
]
