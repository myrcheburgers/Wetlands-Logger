from rest_framework import serializers
from wetland_logger.models import User, Project, Datapoint

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'

class DatapointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datapoint
        fields = '__all__'
