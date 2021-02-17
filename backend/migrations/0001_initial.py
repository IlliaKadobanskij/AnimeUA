# Generated by Django 3.1.3 on 2021-02-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=160, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Bucket',
                'verbose_name_plural': 'Buckets',
            },
        ),
    ]
