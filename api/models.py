from django.db import models


class Note(models.Model):
    id = models.UUIDField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField()
