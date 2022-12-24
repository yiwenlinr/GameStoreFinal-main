# Generated by Django 4.1.3 on 2022-12-07 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('segundaApp', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Videojuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('desarrollador', models.CharField(max_length=50)),
                ('generos', models.CharField(max_length=50)),
                ('plataformas', models.CharField(max_length=50)),
                ('fecha_lanzamiento', models.DateField(default='')),
                ('puntuacion', models.CharField(default='', max_length=2)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='segundaApp.empleados')),
            ],
        ),
    ]