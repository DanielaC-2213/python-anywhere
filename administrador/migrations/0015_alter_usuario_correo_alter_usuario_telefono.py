# Generated by Django 4.0.4 on 2022-05-21 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0014_alter_elemento_foto_alter_elemento_tipo_elemento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=100),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefono',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
