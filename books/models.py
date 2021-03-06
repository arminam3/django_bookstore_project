from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=1000)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='book_covers', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('book_details', args=[self.id])

    def __str__(self):
        return self.title + ' | ' + self.author

