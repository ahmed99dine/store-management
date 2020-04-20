# Generated by Django 3.0.5 on 2020-04-12 21:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_remove_price_model_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='price',
            name='model_no',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='djangoapp.Item'),
            preserve_default=False,
        ),
    ]
