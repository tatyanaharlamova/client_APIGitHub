# Generated by Django 5.1.3 on 2024-11-08 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='git',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Название репозитория'),
        ),
    ]
