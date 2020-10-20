from django.db import models

class door(models.Model):
    wall = models.IntegerField()
    position = models.IntegerField()

class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    width = models.IntegerField()
    length = models.IntegerField()
    door = models.ManyToManyField(Door)