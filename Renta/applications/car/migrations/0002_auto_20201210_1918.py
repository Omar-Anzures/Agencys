# Generated by Django 3.1.2 on 2020-12-10 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carcaratmodel',
            options={'verbose_name_plural': 'Caracteristica Automovil'},
        ),
        migrations.AlterModelOptions(
            name='carmodel',
            options={'verbose_name_plural': 'Automovil'},
        ),
        migrations.AlterField(
            model_name='carmodel',
            name='estado',
            field=models.CharField(blank=True, choices=[('D', 'Disponible'), ('O', 'Ocupado')], default=0, help_text='Estado del automovil', max_length=1),
        ),
    ]