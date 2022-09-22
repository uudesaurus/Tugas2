from logging.handlers import RotatingFileHandler
from django.db import models

class MyWatchList(models.Model):
    watched = models.TextField()
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.IntegerField()
    review = models.TextField()
# Create your models here.
