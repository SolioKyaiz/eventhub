# Generated by Django 5.2 on 2025-04-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='category',
            new_name='categories',
        ),
    ]
