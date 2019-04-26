from django.db import models

# Create your models here.
class Snippet(models.Model):
    ip = models.CharField(max_length=18)
    mask = models.CharField(max_length =18)


    def __str__(self):
        return self.ip,self.mask
