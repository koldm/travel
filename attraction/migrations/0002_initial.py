# Generated by Django 4.0.3 on 2022-03-25 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('attraction', '0001_initial'),
        ('geo', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='attractionreview',
            name='author',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор отзыва'),
        ),
        migrations.AddField(
            model_name='attractionfaq',
            name='attraction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='attraction.attraction', verbose_name='Достопримечательность'),
        ),
        migrations.AddField(
            model_name='attractionfaq',
            name='author_answer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_answer', to=settings.AUTH_USER_MODEL, verbose_name='Автор ответа'),
        ),
        migrations.AddField(
            model_name='attractionfaq',
            name='author_question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='author_question', to=settings.AUTH_USER_MODEL, verbose_name='Автор вопроса'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='city',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geo.city', verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='geo.region', verbose_name='Область/край'),
        ),
        migrations.AddField(
            model_name='attraction',
            name='type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='attraction.attractiontype'),
        ),
    ]
