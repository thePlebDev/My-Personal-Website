# Generated by Django 2.2.7 on 2019-11-07 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_auto_20191107_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_edited',
            field=models.DateField(auto_now=True),
        ),
    ]