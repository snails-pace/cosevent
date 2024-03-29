# Generated by Django 4.2.7 on 2023-12-21 11:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosevent', '0003_rename_owner_event_artist_remove_event_artist_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosevent.event')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosevent.profile')),
            ],
            options={
                'ordering': ['event'],
            },
        ),
    ]
