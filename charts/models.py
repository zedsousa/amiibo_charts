from django.db import models

# Create your models here.
class Chart(models.Model):
    link = models.CharField(max_length=256)

    def __str__(self):
        return self.link