# Generated by Django 2.1.15 on 2020-07-25 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0021_auto_20200724_1022'),
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
            field=models.CharField(choices=[('CS', 'computer science'), ('MHE', 'mechnical engineering'), ('PS', 'political science')], default='computer science', max_length=34),
        ),
        migrations.AlterField(
            model_name='studentdb',
            name='level',
            field=models.CharField(choices=[('500', '500'), ('400', '400'), ('100', '100'), ('300', '300'), ('200', '200')], default='student', max_length=34),
        ),
    ]