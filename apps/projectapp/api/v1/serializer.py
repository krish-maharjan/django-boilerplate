from rest_framework.serializers import ModelSerializer
from apps.projectapp.models import Example


class ExampleSerializer(ModelSerializer):
    class Meta:
        model = Example
        fields = '__all__'
