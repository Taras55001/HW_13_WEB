from django.db import models
from django.contrib.auth.models import User
from quotes.models import Tag



class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=100)
    born_date = models.DateTimeField()
    born_location = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.fullname

class Quote(models.Model):
    quote = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
