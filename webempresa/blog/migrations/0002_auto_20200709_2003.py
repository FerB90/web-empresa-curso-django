# Generated by Django 3.0.6 on 2020-07-09 23:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 9, 23, 3, 35, 18440, tzinfo=utc), verbose_name='Fecha de Publicación'),
        ),
    ]
