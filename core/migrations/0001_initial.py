# Generated by Django 3.1.1 on 2020-09-14 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StartUpInternships',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startup_name', models.CharField(max_length=40)),
                ('startup_contact_name', models.CharField(max_length=30)),
                ('startup_contact_email', models.EmailField(max_length=254)),
                ('startup_contact_phone', models.IntegerField()),
                ('incentive', models.IntegerField()),
                ('description_file', models.FileField(upload_to='')),
                ('startup_website', models.URLField()),
            ],
        ),
    ]