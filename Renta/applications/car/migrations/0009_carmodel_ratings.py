# Generated by Django 3.1.2 on 2021-01-18 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0008_carmodel_tamano'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='ratings',
            field=models.PositiveIntegerField(default=0),
        ),
    ]