# Generated by Django 3.1.1 on 2020-09-14 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='startupinternships',
            name='startup_contact_phone',
            field=models.CharField(max_length=20),
        ),
    ]
