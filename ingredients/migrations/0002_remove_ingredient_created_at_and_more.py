# Generated by Django 4.1.6 on 2023-08-04 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='updated_at',
        ),
    ]