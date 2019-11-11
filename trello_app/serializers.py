from rest_framework import serializers
from .models import BroadTopics, SubTopics, Items


class ItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Items
        fields = ['id', 'description', 'status', 'priority']


class SubtopicSerializer(serializers.ModelSerializer):
    items = ItemsSerializer(many=True, read_only=True)

    class Meta:
        model = SubTopics
        fields = ['id', 'title', 'items', 'status']


class BroadTopicsSerializer(serializers.ModelSerializer):
    subtopics = SubtopicSerializer(many=True, read_only=True)

    class Meta:
        model = BroadTopics
        fields = ['id', 'title', 'subtopics', 'status']
