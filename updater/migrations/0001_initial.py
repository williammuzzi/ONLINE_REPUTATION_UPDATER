# Generated by Django 5.1.6 on 2025-03-03 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POI',
            fields=[
                ('poiid', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('dealerid', models.CharField(max_length=50)),
                ('email_poc', models.EmailField(max_length=254)),
                ('ordered_timestamp', models.DateTimeField(null=True)),
                ('ordered', models.BooleanField(default=False)),
            ],
        ),
    ]
