# Generated by Django 2.1.3 on 2019-06-18 03:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Bootcamp', max_length=200)),
                ('venue', models.CharField(default='Arun Thapa Chowk', max_length=300)),
                ('description', models.TextField(default='Lorem ipsum doler sit amet.')),
                ('image', models.ImageField(upload_to='bootcamp/static/bootcamp/site-data/events')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Main_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Bootcamp', max_length=200)),
                ('venue', models.CharField(default='Arun Thapa Chowk', max_length=300)),
                ('description', models.TextField(default='Lorem ipsum doler sit amet.')),
                ('image', models.ImageField(upload_to='bootcamp/static/bootcamp/site-data/main-events')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]