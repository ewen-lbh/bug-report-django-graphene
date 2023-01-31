from django.db import models

class Test(models.Model):
    testing = models.CharField(max_length=100)
