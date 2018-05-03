from django.db import models


class Voter(models.Model):
    name = models.CharField(max_length=200)
    guardian = models.CharField(max_length=200)
    guardianType = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    sno = models.CharField(max_length=200)
    voterId = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

