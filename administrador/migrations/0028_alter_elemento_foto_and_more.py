# Generated by Django 4.0.3 on 2022-05-25 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0027_electrodomestico_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elemento',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='carrito'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='porcentaje_ganancia',
            field=models.CharField(choices=[('0.1', '10%'), ('0.15', '15%'), ('0.2', '20%'), ('0.3', '30%')], max_length=10, verbose_name='Porcentaje'),
        ),
        migrations.AlterField(
            model_name='elemento',
            name='precio',
            field=models.IntegerField(verbose_name='Precio'),
        ),
    ]
