# Generated by Django 3.0.7 on 2020-07-13 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20200713_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='permoted_product',
            field=models.BooleanField(default=False),
        ),
    ]