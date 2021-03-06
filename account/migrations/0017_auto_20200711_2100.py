# Generated by Django 3.0.7 on 2020-07-11 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20200711_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdb',
            name='StudentCourse',
            field=models.CharField(choices=[('CS', 'computer science'), ('MHE', 'mechnical engineering'), ('PS', 'political science')], default='computer science', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='level',
            field=models.CharField(choices=[('500', '500'), ('300', '300'), ('200', '200'), ('400', '400'), ('100', '100')], default='student', max_length=34),
        ),
    ]
