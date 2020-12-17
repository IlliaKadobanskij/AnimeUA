# Generated by Django 3.1.3 on 2020-12-17 21:13

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=150, verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=150, verbose_name='Genre')),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video', models.FileField(default=None, upload_to='', verbose_name='Video')),
                ('bucket_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.bucket')),
            ],
            options={
                'verbose_name': 'Video',
                'verbose_name_plural': 'Videos',
            },
        ),
        migrations.CreateModel(
            name='ShadowMovie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, verbose_name='Title')),
                ('description', models.TextField(default=None, verbose_name='Description')),
                ('poster', models.ImageField(default=None, upload_to='actors/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='Release date')),
                ('country', models.CharField(default=None, max_length=30, verbose_name='Country')),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=30), default=None, size=None)),
                ('url', models.SlugField(default=None, max_length=130, unique=True)),
                ('rating', models.FloatField(default=None, max_length=10, verbose_name='Rating')),
                ('video_urls', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=None, max_length=200), default=None, size=None)),
                ('movie_id', models.IntegerField(default=0, verbose_name='Movie id')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default=None, max_length=100, verbose_name='Title')),
                ('description', models.TextField(default=None, verbose_name='Description')),
                ('poster', models.ImageField(default=None, upload_to='actors/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='Release date')),
                ('country', models.CharField(default=None, max_length=30, verbose_name='Country')),
                ('url', models.SlugField(default=None, max_length=130, unique=True)),
                ('rating', models.FloatField(default=None, max_length=10, verbose_name='Rating')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.category', verbose_name='Category')),
                ('genres', models.ManyToManyField(default=None, to='movie.Genre', verbose_name='Genres')),
                ('video', models.ManyToManyField(default=None, to='movie.Video', verbose_name='Video')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
