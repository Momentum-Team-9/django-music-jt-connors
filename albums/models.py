from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Albums(models.Model):
    title = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.artist}"

class Tracks(models.Model):
    title = models.CharField(max_length=250)
    album = models.ForeignKey(Albums, on_delete=models.CASCADE, related_name="tracks")

    def __str__(self):
        return f"{self.title}, {self.album}"
