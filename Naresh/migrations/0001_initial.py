# Generated by Django 3.0.6 on 2020-06-07 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField()),
                ('web', models.URLField(null=True)),
                ('phone', models.IntegerField()),
                ('age', models.IntegerField()),
                ('degree', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('freelancing', models.CharField(max_length=200, null=True)),
                ('notes', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interest', models.CharField(max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=300)),
                ('percent', models.IntegerField()),
            ],
        ),
    ]
