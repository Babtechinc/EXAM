# Generated by Django 3.0.7 on 2020-06-30 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20200630_0907'),
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
            field=models.CharField(choices=[('200', '200'), ('100', '100'), ('500', '500'), ('300', '300'), ('400', '400')], default='student', max_length=34),
        ),
    ]