# Generated by Django 2.2.7 on 2019-11-21 04:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0018_auto_20191119_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='urls',
            field=models.URLField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]