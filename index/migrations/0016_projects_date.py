# Generated by Django 2.2.7 on 2019-11-18 01:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_projects'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]