# Generated by Django 3.2.16 on 2024-02-25 10:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254, unique=True),
            preserve_default=False,
        ),
    ]