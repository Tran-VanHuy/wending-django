# Generated by Django 4.2.3 on 2024-04-08 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0004_guestbooknumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='guestbooknumber',
            old_name='full_name',
            new_name='name',
        ),
    ]
