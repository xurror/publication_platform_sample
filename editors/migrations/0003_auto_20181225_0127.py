# Generated by Django 2.1.4 on 2018-12-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editors', '0002_auto_20181225_0112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editors',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]
