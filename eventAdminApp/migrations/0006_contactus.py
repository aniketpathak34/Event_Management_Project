# Generated by Django 4.1.7 on 2023-03-01 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventAdminApp', '0005_videocontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=13)),
                ('message', models.TextField()),
            ],
        ),
    ]
