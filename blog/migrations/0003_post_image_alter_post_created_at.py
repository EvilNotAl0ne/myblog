# Generated by Django 5.1 on 2024-09-02 17:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Опубликовано'),
        ),
    ]