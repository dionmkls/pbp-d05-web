# Generated by Django 3.2.7 on 2021-12-28 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VaksinBekasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=24)),
                ('url', models.CharField(max_length=1000)),
                ('alamat', models.CharField(max_length=63)),
                ('nomorTelp', models.IntegerField()),
                ('jenis', models.CharField(max_length=63)),
                ('syaratPeserta', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='VaksinBogor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=24)),
                ('url', models.CharField(max_length=1000)),
                ('alamat', models.CharField(max_length=63)),
                ('nomorTelp', models.IntegerField()),
                ('jenis', models.CharField(max_length=63)),
                ('syaratPeserta', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='VaksinDepok',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=24)),
                ('url', models.CharField(max_length=1000)),
                ('alamat', models.CharField(max_length=63)),
                ('nomorTelp', models.IntegerField()),
                ('jenis', models.CharField(max_length=63)),
                ('syaratPeserta', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='VaksinJakarta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=24)),
                ('url', models.CharField(max_length=1000)),
                ('alamat', models.CharField(max_length=63)),
                ('nomorTelp', models.IntegerField()),
                ('jenis', models.CharField(max_length=63)),
                ('syaratPeserta', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='VaksinTangerang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=24)),
                ('url', models.CharField(max_length=1000)),
                ('alamat', models.CharField(max_length=63)),
                ('nomorTelp', models.IntegerField()),
                ('jenis', models.CharField(max_length=63)),
                ('syaratPeserta', models.CharField(max_length=63)),
            ],
        ),
    ]
