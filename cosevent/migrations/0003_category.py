# Generated by Django 4.2.7 on 2023-11-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosevent', '0002_alter_event_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
    ]
