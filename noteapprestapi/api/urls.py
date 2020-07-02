from django.urls import include, path 
from rest_framework import routers
from .views import NoteViewSet, TagViewSet, UserViewSet

router = routers.DefaultRouter()
router.register(r'tags', TagViewSet)
router.register(r'notes', NoteViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
  path('', include(router.urls))
]