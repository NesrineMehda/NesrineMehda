from django.db import models

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()

    def __str__(self):
        return self.title

class Photo(models.Model):
    album = models.ForeignKey(Album, related_name='photos', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return self.description

