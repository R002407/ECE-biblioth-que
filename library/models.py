from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    published_date = models.DateField(null=True, blank=True)
    category = models.CharField(max_length=100, blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.author}"
