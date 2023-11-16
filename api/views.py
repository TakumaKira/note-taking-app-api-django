from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import NoteSerializer
from api.models import Note


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows note to be viewed or edited.
    """
    queryset = Note.objects.all().order_by('-created_at')
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]
