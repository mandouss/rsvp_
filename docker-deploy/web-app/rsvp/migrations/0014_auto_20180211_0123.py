# Generated by Django 2.0.1 on 2018-02-11 01:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rsvp', '0013_response_freetext_question_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response_freetext',
            new_name='ResponseFreetext',
        ),
    ]
