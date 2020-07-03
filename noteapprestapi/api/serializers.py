from rest_framework import serializers
from .models import User, Tag, Note


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email')


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('name', 'id')


class NoteSerializer(serializers.ModelSerializer):
    tag = serializers.StringRelatedField(many=True)
    user = serializers.StringRelatedField()
    class Meta:
        model = Note
        fields = ('creation_date', 'end_date', 'note',
                  'is_task', 'user', 'tag', 'attachment', 'note_type')
