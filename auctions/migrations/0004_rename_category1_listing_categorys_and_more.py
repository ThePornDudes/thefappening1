# Generated by Django 4.0.3 on 2022-04-01 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_category1_listing_category2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='category1',
            new_name='categorys',
        ),
        migrations.RenameField(
            model_name='listing',
            old_name='category2',
            new_name='categoryss',
        ),
    ]