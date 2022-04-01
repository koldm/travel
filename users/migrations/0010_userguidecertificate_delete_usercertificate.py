# Generated by Django 4.0.3 on 2022-03-30 16:34

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_usercertificate_small_certificate_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGuideCertificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.ImageField(upload_to=users.models.user_guide_certificate_path)),
                ('small_certificate', imagekit.models.fields.ProcessedImageField(upload_to=users.models.user_guide_certificate_path)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.userguide', verbose_name='Гид')),
            ],
            options={
                'verbose_name': 'Сертификат гида',
                'verbose_name_plural': 'Сертификаты гидов',
            },
        ),
        migrations.DeleteModel(
            name='UserCertificate',
        ),
    ]
