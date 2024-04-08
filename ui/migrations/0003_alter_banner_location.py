# Generated by Django 4.2.3 on 2024-04-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0002_alter_banner_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='location',
            field=models.IntegerField(blank=True, choices=[(1, 'Vị trí 1'), (2, 'Vị trí 2'), (3, 'Vị trí 3'), (4, 'Vị trí 4')], null=True, verbose_name='Vị trí'),
        ),
    ]