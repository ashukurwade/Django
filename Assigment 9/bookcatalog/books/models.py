

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True)
    pages = models.PositiveIntegerField()
    cover_image_url = models.URLField(blank=True)

    def __str__(self):
        return self.title