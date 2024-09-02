from django.urls import path
from .views import UserListCreateAPIView, ProjectListCreateAPIView, ProjectDetailAPIView, TemplateCreateApiView, TemplateDetailAPIView, LayerListCreateAPIView, LayerDetailAPIView, LayerListCreateAPIView, LayerDetailAPIView, AssentListCreateAPIView, AssentDtailAPIView

urlpatterns = [
    path('users/', UserListCreateAPIView.as_view(), name='user-list-create'),
    path('projects/', ProjectListCreateAPIView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('templates/', TemplateCreateApiView.as_view(), name='templates-list-create'),
    path('templates/<int:pk>/', TemplateDetailAPIView.as_view(), name='templates-detail'),
    path('layers/',LayerListCreateAPIView.as_view(), name='layers-list-create'),
    path('layers/<int:pk>/', LayerDetailAPIView.as_view(), name='layers-detail'),
    path('assents/',AssentListCreateAPIView.as_view(), name='assents-list-create'),
    path('assents/<int:pk>/', AssentDtailAPIView.as_view(), name='assents-detail'),
    # Añade rutas para templates, layers, y assets según sea necesario
]