# Generated by Django 2.2.24 on 2021-11-04 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oksigen', '0002_oksigen_domisili'),
    ]

    operations = [
        migrations.AlterField(
            model_name='oksigen',
            name='domisili',
            field=models.CharField(choices=[('Jakarta', 'Jakarta'), ('Bogor', 'Bogor'), ('Depok', 'Depok'), ('Tangerang', 'Tangerang'), ('Bekasi', 'Bekasi')], default='green', max_length=9),
        ),
    ]