from django.db import models
#from django.contrib.postgres.fields import ArrayField

# Create your models here.
class PointSet(models.Model):
    UUID = models.UUIDField(max_length=200)
    date = models.DateTimeField('Date of landmarking')
    session = models.IntegerField()
    subject = models.CharField(max_length=200)
    template = models.FileField(upload_to=None, max_length=200)
#    error = ArrayField(models.FloatField(), size=None)
#    point = ArrayField(models.FloatField(), size=None)
    
class Fiducial(models.Model):
    PUID = models.UUIDField(max_length=200)
    location = models.CharField(max_length=1)
    pair = models.IntegerField()
    template = models.FileField(upload_to=None, max_length=200)