# Generated by Django 4.2.7 on 2023-11-05 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date', models.DateTimeField()),
                ('venue', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=20)),
                ('availability', models.PositiveIntegerField()),
                ('artist_name', models.CharField(max_length=255)),
            ],
        ),
    ]
