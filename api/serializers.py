from rest_framework import serializers


class NoteSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField(max_length=50)
    content = serializers.CharField(max_length=200)
    created_at = serializers.DateTimeField()
