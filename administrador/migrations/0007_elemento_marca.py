# Generated by Django 4.0.3 on 2022-05-18 18:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0006_alter_usuario_telefono'),
    ]

    operations = [
        migrations.AddField(
            model_name='elemento',
            name='marca',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrador.marca', verbose_name='Marca'),
        ),
    ]
