# Generated by Django 3.0.7 on 2020-07-26 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0027_product_search_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerorder',
            name='expected_date',
            field=models.DateField(null=True),
        ),
    ]