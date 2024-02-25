from django.db import models
from django.contrib.auth.models import AbstractBaseUser



class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    is_patient = models.BooleanField(default=False)
    is_counsellor = models.BooleanField(default=False)


class Patient(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'patient'
