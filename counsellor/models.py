from django.db import models


class Counsellor(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'counsellor'