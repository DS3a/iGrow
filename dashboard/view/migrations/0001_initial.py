# Generated by Django 3.1.7 on 2021-03-19 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='values',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Temperature', models.CharField(max_length=10)),
                ('Pressure', models.CharField(max_length=10)),
                ('Humidity', models.CharField(max_length=10)),
                ('pH', models.CharField(max_length=10)),
                ('Intensity', models.CharField(max_length=10)),
            ],
        ),
    ]
