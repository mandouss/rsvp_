# Generated by Django 2.0.2 on 2018-02-12 03:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rsvp', '0015_auto_20180211_0247'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='response',
            name='event',
        ),
    ]