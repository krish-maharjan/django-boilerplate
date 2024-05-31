from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.projectapp.api.v1.views import ExampleViewSets


router = DefaultRouter()
router.register(r'example', ExampleViewSets)

urlpatterns = [
    path('api/v1/', include(router.urls))
]
