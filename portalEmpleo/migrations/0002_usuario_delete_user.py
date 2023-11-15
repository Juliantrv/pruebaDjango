# Generated by Django 4.2.7 on 2023-11-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalEmpleo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_perfil', models.TextField(blank=True, verbose_name='Descripción del perfil')),
                ('numero_identificacion', models.IntegerField(default=0, verbose_name='Numero de identificación')),
                ('celular', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]