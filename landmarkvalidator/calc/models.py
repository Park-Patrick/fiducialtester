from __future__ import unicode_literals
from django.db import models


class PointSet(models.Model):
    # UUID for pointset
    UUID = models.UUIDField(max_length=200)
    # Date of upload
    date = models.DateTimeField('Date of landmarking')
    # Session for user (mannually specified)
    session = models.IntegerField()
    # Subject
    subject = models.CharField(max_length=200)
    # Template brain
    template = models.CharField(max_length=200)
    # 4 by n array of x, y, z, and euclidean error
    error = models.FileField(upload_to=None, max_length=200)
    # pointset of fiducials
    point = models.FileField(upload_to=None, max_length=200)
    
class Fiducial(models.Model):
    # UUID for fiducial
    PUID = models.UUIDField(max_length=200)
    # Location (medial, right, or left)
    location = models.CharField(max_length=1)
    # If right or left the pair point, if not -1
    pair = models.IntegerField()
    # Template brain
    template = models.CharField(max_length=200)

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='db_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
