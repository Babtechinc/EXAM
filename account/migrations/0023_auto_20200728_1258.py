# Generated by Django 2.1.15 on 2020-07-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20200725_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roleUser',
            field=models.CharField(choices=[('teacher', 'teacher'), ('student', 'student')], default='student', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='StudentCourse',
            field=models.CharField(choices=[('MHE', 'mechnical engineering'), ('PS', 'political science'), ('CS', 'computer science')], default='computer science', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='level',
            field=models.CharField(choices=[('200', '200'), ('100', '100'), ('300', '300'), ('500', '500'), ('400', '400')], default='student', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='semester',
            field=models.CharField(choices=[('2', '2'), ('1', '1')], default='1', max_length=34),
        ),
    ]
