# Generated by Django 3.1.7 on 2021-03-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('digipackDB', '0002_remove_student_credentials'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='credentials',
            field=models.JSONField(default=''),
        ),
    ]
