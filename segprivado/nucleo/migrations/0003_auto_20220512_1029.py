# Generated by Django 3.1.2 on 2022-05-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nucleo', '0002_auto_20220512_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_active',
            field=models.SmallIntegerField(default=False, verbose_name='Activo'),
        ),
    ]
