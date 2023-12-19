# Generated by Django 5.0 on 2023-12-19 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('rate', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='mvpic')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('rate', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='mvpic')),
                ('desc', models.TextField()),
            ],
        ),
    ]
