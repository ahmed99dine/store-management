# Generated by Django 3.0.5 on 2020-04-12 20:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='model_no',
            field=models.OneToOneField(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, related_name='price_model_no', to='djangoapp.Item'),
            preserve_default=False,
        ),
    ]
