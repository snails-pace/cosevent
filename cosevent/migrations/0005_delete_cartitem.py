# Generated by Django 4.2.7 on 2023-12-30 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosevent', '0004_cartitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]