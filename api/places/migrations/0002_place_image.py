# Generated by Django 4.0.3 on 2023-04-20 19:37

from django.db import migrations, models
import places.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to=places.models.upload_load),
        ),
    ]
