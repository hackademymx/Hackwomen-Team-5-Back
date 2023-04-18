from django.db import models

class Users(models.Model):
    username =models.CharField (max_length=32)
    email = models.CharField (max_length=56)
    password = models.CharField (max_length=32)

