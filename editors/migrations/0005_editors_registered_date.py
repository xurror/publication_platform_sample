# Generated by Django 2.1.4 on 2018-12-25 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0004_editors_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='editors',
            name='registered_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]