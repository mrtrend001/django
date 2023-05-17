from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    description = models.TextField()
    type_book = models.TextField()
    genre = models.TextField(max_length=150)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
