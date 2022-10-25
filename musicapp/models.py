#!/usr/bin/env python

from django.db import models

# Create your models here.
class Song(models.Model):
    Artiste = models.TextField()
    Song = models.TextField()
    Lyric =models.TextField()

    def __str__(self):
        return self.title
