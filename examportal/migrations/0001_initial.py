# Generated by Django 3.0.7 on 2020-06-08 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(blank=None, max_length=1000)),
                ('answer', models.CharField(blank=None, max_length=1000)),
                ('option1', models.CharField(blank=None, max_length=1000)),
                ('option2', models.CharField(blank=None, max_length=1000)),
                ('option3', models.CharField(blank=None, max_length=1000)),
                ('option4', models.CharField(blank=None, max_length=1000)),
            ],
        ),
    ]