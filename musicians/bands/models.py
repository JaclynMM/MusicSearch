from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    hometown = models.CharField(max_length=150)
    twitter_id = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Band(models.Model):
    members = models.ManyToManyField(Artist)
    name = models.CharField(max_length=150)
    genre = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    hometown = models.CharField(max_length=150)
    website = models.URLField(blank=True)
    twitter_id = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    band = models.ForeignKey(Band)
    name = models.CharField(max_length=150)
    create_date= models.DateField()

    def __str__(self):
        return self.name
