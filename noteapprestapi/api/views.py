from rest_framework import viewsets

from .serializers import UserSerializer, TagSerializer, NoteSerializer
from .models import User, Tag, Note

class NoteViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all().order_by('end_date')
  serializer_class = NoteSerializer

class TagViewSet(viewsets.ModelViewSet):
  queryset = Tag.objects.all()
  serializer_class = TagSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = Note.objects.all().order_by('name')
  serializer_class = UserSerializer