# Generated by Django 4.0.3 on 2022-03-31 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_category_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='text',
            field=models.TextField(blank=True, default='', verbose_name='Текст раздела'),
            preserve_default=False,
        ),
    ]