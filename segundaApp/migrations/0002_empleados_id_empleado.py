# Generated by Django 4.1.3 on 2022-12-07 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('segundaApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='id_empleado',
            field=models.CharField(default='', max_length=50),
        ),
    ]
