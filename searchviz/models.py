from django.db import models


# Create your models here.
class SearchName(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(default=" ", max_length=50)

    def __str__(self):
        return "Name:{0}".format(self.name)
