# Generated by Django 5.1.7 on 2025-03-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('available', models.BooleanField(default=True)),
            ],
        ),
    ]
