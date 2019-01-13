from django.db import models



class Artist(models.Model):
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Song(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Fact(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    publisher_name = models.CharField(max_length=100)

    def __str__(self):
        return self.text
