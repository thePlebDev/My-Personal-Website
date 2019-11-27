# Generated by Django 2.2.7 on 2019-11-18 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0014_auto_20191114_0026'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('about', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
    ]
