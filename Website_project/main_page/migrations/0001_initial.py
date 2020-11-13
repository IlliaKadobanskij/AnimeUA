# Generated by Django 3.1.3 on 2020-11-12 22:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Age')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Actors and directors',
                'verbose_name_plural': 'Actors and directors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Category')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=160, unique=True)),
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
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Genre',
                'verbose_name_plural': 'Genres',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Tagline')),
                ('description', models.TextField(verbose_name='Description')),
                ('poster', models.ImageField(upload_to='actors/', verbose_name='Poster')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='Release date')),
                ('country', models.CharField(max_length=30, verbose_name='Country')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='World premiere')),
                ('budget', models.PositiveIntegerField(default=0, help_text='Amount in dollars', verbose_name='Budget')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='Amount in dollars', verbose_name='Fees in USA')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='Amount in dollars', verbose_name='Fees in world')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Draft')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='main_page.Actor', verbose_name='actors')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_page.category', verbose_name='Category')),
                ('directors', models.ManyToManyField(related_name='film_director', to='main_page.Actor', verbose_name='producer')),
                ('genres', models.ManyToManyField(to='main_page.Genre', verbose_name='genres')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Value')),
            ],
            options={
                'verbose_name': 'RatingStar',
                'verbose_name_plural': 'RatingStars',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=160, verbose_name='name')),
                ('text', models.TextField(max_length=5000, verbose_name='Text')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.movie', verbose_name='Movie')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_page.reviews', verbose_name='Parent')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='IP address')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.movie', verbose_name='Movie')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.ratingstar', verbose_name='Star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(upload_to='actors/', verbose_name='Image')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_page.movie', verbose_name='Movie')),
            ],
            options={
                'verbose_name': 'MovieShot',
                'verbose_name_plural': 'MovieShots',
            },
        ),
    ]
