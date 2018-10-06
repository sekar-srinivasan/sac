from django.urls import path
from .views import(
    PartnerView,
)
from child.views import(
    ChildCreateView,
    ChildDetailView,
    ChildListView,
    ChildUpdateView,
    ChildDeleteView,
)

app_name = 'partner'
urlpatterns = [
    path('', PartnerView.as_view(), name='partner'),

    # path('create/<int:project_pk>', ChildCreateView.as_view(), name='child-create'),
    # path('<int:pk>/', ChildDetailView.as_view(), name='child-detail'),
    # path('', ChildListView.as_view(), name='child-list'),
    # path('<int:pk>/update/', ChildUpdateView.as_view(), name='child-update'),
    # path('<int:pk>/delete/', ChildDeleteView.as_view(), name='child-delete'),
]
