# Generated by Django 3.1.2 on 2020-12-10 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20201210_1945'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carmodel',
            name='nombre',
        ),
    ]