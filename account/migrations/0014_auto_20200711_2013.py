# Generated by Django 3.0.7 on 2020-07-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20200711_2006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdb',
            name='StudentCourse',
            field=models.CharField(choices=[('MHE', 'mechnical engineering'), ('CS', 'computer science'), ('PS', 'political science')], default='computer science', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='level',
            field=models.CharField(choices=[('100', '100'), ('400', '400'), ('300', '300'), ('200', '200'), ('500', '500')], default='student', max_length=34),
        ),
    ]