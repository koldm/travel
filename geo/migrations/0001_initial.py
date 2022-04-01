# Generated by Django 4.0.3 on 2022-03-25 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название области')),
                ('name_pr', models.CharField(blank=True, max_length=255, verbose_name='Название области в предложном падеже')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('url', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'Область/край',
                'verbose_name_plural': 'Области/края',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Название города')),
                ('name_pr', models.CharField(blank=True, max_length=255, verbose_name='Название города в предложном падеже')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активность')),
                ('url', models.SlugField(max_length=255, unique=True, verbose_name='URL')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geo.region', verbose_name='Область/край')),
            ],
            options={
                'verbose_name': 'Город',
                'verbose_name_plural': 'Города',
                'ordering': ['name'],
            },
        ),
    ]