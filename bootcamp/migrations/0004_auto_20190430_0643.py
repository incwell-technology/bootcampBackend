# Generated by Django 2.1.3 on 2019-04-30 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllabus', '0002_auto_20190430_0643'),
        ('bootcamp', '0003_auto_20190430_0457'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='first_name',
            new_name='firstName',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='last_name',
            new_name='lastName',
        ),
        migrations.AddField(
            model_name='mentor',
            name='course',
            field=models.ManyToManyField(related_name='mentor_course', to='syllabus.Course'),
        ),
    ]
