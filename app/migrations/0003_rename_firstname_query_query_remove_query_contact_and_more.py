# Generated by Django 4.0.2 on 2024-01-12 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_query'),
    ]

    operations = [
        migrations.RenameField(
            model_name='query',
            old_name='Firstname',
            new_name='Query',
        ),
        migrations.RemoveField(
            model_name='query',
            name='Contact',
        ),
        migrations.RemoveField(
            model_name='query',
            name='Lastname',
        ),
    ]
