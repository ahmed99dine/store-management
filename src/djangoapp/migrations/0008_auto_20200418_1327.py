# Generated by Django 3.0.5 on 2020-04-18 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0007_auto_20200413_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='price',
            old_name='item',
            new_name='item_id',
        ),
    ]