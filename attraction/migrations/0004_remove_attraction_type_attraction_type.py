# Generated by Django 4.0.3 on 2022-03-27 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attraction', '0003_attraction_average_rating_attraction_count_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attraction',
            name='type',
        ),
        migrations.AddField(
            model_name='attraction',
            name='type',
            field=models.ManyToManyField(blank=True, to='attraction.attractiontype'),
        ),
    ]
