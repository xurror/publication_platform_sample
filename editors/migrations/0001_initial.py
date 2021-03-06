# Generated by Django 2.1.4 on 2018-12-25 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Editors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('phone', models.IntegerField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('is_mvp', models.BooleanField(default=False)),
            ],
        ),
    ]
