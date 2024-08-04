from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.projectapp.api.v1.views import (ExampleViewSets, CachedExampleViewSets,
                                          CeleryTaskViewSets)


router = DefaultRouter()
router.register(r'example', ExampleViewSets, basename="Example")
router.register(r'cachedexample', CachedExampleViewSets, basename="CachedExample")
router.register(r'celerywork', CeleryTaskViewSets, basename="CeleryTase")

urlpatterns = [
    path('api/v1/', include(router.urls))
]
