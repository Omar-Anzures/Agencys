# Generated by Django 3.1.2 on 2020-12-11 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0005_remove_carmodel_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='carmodel',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='autos'),
        ),
    ]
