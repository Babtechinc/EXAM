# Generated by Django 3.0.7 on 2020-07-11 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0017_auto_20200711_2100'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseCode', models.CharField(max_length=11)),
                ('CourseName', models.CharField(max_length=120)),
                ('Courses', models.CharField(choices=[('CS', 'computer science'), ('MHE', 'mechnical engineering'), ('PS', 'political science')], default='computer science', max_length=34)),
                ('level', models.CharField(choices=[('500', '500'), ('300', '300'), ('200', '200'), ('400', '400'), ('100', '100')], default='student', max_length=34)),
            ],
        ),
        migrations.CreateModel(
            name='CourseRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CourseCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courseDetail.CourseInfo')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.StudentDB')),
            ],
        ),
    ]
