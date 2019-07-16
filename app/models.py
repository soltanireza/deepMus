from django.db import models


class Tech(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Content(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Sticker(models.Model):
    title = models.CharField(max_length=50, default="title")
    icon = models.CharField(max_length=200, default="icon")
    text = models.TextField(blank=True, default="text")

    def __str__(self):
        return self.title
