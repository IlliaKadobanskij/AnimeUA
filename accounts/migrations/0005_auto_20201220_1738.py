# Generated by Django 3.1.3 on 2020-12-20 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20201220_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercabinet',
            name='avatar',
            field=models.ImageField(default='avatars/10.jpg', upload_to='', verbose_name='Avatar'),
        ),
    ]