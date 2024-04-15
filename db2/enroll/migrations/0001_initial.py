# Generated by Django 4.1.6 on 2023-03-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stuRoll', models.IntegerField()),
                ('stuName', models.CharField(max_length=70)),
                ('stuEmail', models.CharField(max_length=70)),
                ('stuDOB', models.DateField()),
            ],
        ),
    ]
