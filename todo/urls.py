# todo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TodoViewSet

# The DefaultRouter handles routing for the ViewSet.
# It automatically generates URLs for list, create, retrieve, etc.
router = DefaultRouter()
router.register(r'todos', TodoViewSet)

urlpatterns = [
    # Include the router's URLs. The router handles the 'todos/' part of the path.
    path('', include(router.urls)),
]



