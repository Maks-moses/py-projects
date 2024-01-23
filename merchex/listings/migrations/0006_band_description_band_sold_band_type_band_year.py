# Generated by Django 5.0.1 on 2024-01-15 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0005_band_active_band_biography_band_genre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='band',
            name='description',
            field=models.CharField(default='', max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='sold',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='band',
            name='type',
            field=models.CharField(choices=[('REC', 'Records'), ('Clothes', 'Clothing'), ('Posters', 'Posters'), ('Miscellaneous', 'Miscellaneous')], default='Rec', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='band',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
