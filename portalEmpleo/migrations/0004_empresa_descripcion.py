# Generated by Django 4.2.7 on 2023-11-15 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portalEmpleo', '0003_usuario_fecha_nacimiento_usuario_profesion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
    ]