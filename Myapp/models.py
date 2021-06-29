from django.db import models

# Create your models here.
class Details(models.Model):
    objects = None
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=500)
    number = models.CharField(max_length=12)

    class Meta:
        managed = True
        db_table = 'details'
