from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users, Project, Template, Layer, Asset

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['userName', 'email', 'password']

    def create(self, validated_data):
        user = Users(
            userName=validated_data['userName'],
            email=validated_data['email'],
            password=make_password(validated_data['password'])
        )
        user.save()
        return user    
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class TemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Template
        fields = '__all__'

class LayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Layer
        fields = '__all__'

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'
