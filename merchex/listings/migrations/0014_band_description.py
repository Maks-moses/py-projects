# Generated by Django 5.0.1 on 2024-01-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_rename_year_formed_band_annee_de_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]