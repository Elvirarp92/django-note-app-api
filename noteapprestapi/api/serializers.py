from rest_framework import serializers
from .models import User, Tag, Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name')


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('creation_date', 'end_date', 'note',
                  'is_task', 'attachment', 'note_type')
