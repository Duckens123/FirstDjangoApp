# Generated by Django 4.0.6 on 2022-07-18 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listings'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Listings',
            new_name='Listing',
        ),
    ]