# Generated by Django 5.0.1 on 2024-01-21 11:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_remove_title_like_new'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='band',
            name='description',
        ),
        migrations.RemoveField(
            model_name='band',
            name='sold',
        ),
        migrations.RemoveField(
            model_name='band',
            name='year',
        ),
    ]
