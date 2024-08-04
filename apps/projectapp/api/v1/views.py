from rest_framework import viewsets
from rest_framework.response import Response
from django.views.decorators.cache import cache_page

from apps.projectapp.models import Example
from apps.projectapp.serializer import ExampleSerializer
from apps.projectapp.tasks import example_task


# Create your views here.
class ExampleViewSets(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class CachedExampleViewSets(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    @cache_page(60 * 15)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class CeleryTaskViewSets(viewsets.ReadOnlyModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer

    def trigger_task(request):
        example_task.delay('value1', 'value2')
        return Response({'status': 'Task is being processed'})
