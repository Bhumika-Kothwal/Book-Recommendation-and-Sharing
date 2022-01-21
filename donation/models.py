from django.contrib.gis.db import models

class NGO(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)