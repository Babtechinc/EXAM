# Generated by Django 3.0.7 on 2020-07-11 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20200711_0903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roleUser',
            field=models.CharField(choices=[('student', 'student'), ('teacher', 'teacher')], default='student', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='StudentCourse',
            field=models.CharField(choices=[('MHE', 'mechnical engineering'), ('PS', 'political science'), ('CS', 'computer science')], default='computer science', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='level',
            field=models.CharField(choices=[('100', '100'), ('500', '500'), ('200', '200'), ('400', '400'), ('300', '300')], default='student', max_length=34),
        ),
    ]
