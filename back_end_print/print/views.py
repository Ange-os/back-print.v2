from rest_framework import generics
from .models import Users, Project, Template, Layer, Asset
from .serializers import UserSerializer, ProjectSerializer, TemplateSerializer, LayerSerializer, AssetSerializer

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TemplateCreateApiView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class TemplateDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer

class LayerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer

class LayerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Layer.objects.all()
    serializer_class = LayerSerializer

class AssentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssentDtailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer        