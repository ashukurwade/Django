from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_date = models.DateField()
    isbn = models.CharField(max_length=13, unique=True)
    description = models.TextField(blank=True, null=True)
    pages = models.IntegerField()
    cover_image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title