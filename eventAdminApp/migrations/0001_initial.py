# Generated by Django 4.1.7 on 2023-02-25 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventName', models.CharField(max_length=200)),
                ('eventPlace', models.CharField(max_length=100)),
                ('eventDescription', models.CharField(max_length=1000)),
                ('eventDate', models.DateField()),
                ('eventImageOne', models.FileField(default=None, max_length=300, null=True, upload_to='clientgallery/')),
                ('eventImageTwo', models.FileField(default=None, max_length=300, null=True, upload_to='clientgallery/')),
                ('eventImageThree', models.FileField(default=None, max_length=300, null=True, upload_to='clientgallery/')),
            ],
        ),
    ]
