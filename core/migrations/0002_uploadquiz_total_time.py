# Generated by Django 4.1.5 on 2023-01-15 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadquiz',
            name='total_time',
            field=models.CharField(default='1 hour', max_length=255),
        ),
    ]
