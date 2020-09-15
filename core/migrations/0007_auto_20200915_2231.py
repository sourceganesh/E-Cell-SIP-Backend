# Generated by Django 3.1.1 on 2020-09-15 17:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_startupinternships_last_date_to_apply'),
    ]

    operations = [
        migrations.AddField(
            model_name='startupinternships',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='startupinternships',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
