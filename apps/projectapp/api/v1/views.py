from rest_framework import viewsets
from apps.projectapp.models import Example
from apps.projectapp.api.v1.serializer import ExampleSerializer


# Create your views here.
class ExampleViewSets(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
