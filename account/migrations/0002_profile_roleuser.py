# Generated by Django 3.0.7 on 2020-06-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roleUser',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=34),
        ),
    ]
