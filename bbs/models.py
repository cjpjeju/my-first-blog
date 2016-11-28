# Create your models here.
from django.db import models


# Create your models here.
class Guestbook(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title

    def savedata(self, t, e, c):
        self.title = t
        self.email = e
        self.content = c

        self.save()