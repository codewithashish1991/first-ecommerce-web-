# Generated by Django 3.0.7 on 2020-07-23 07:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_auto_20200723_1159'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Customer_Order',
            new_name='CustomerOrder',
        ),
        migrations.RenameModel(
            old_name='Customer_Review',
            new_name='CustomerReview',
        ),
        migrations.RenameModel(
            old_name='Customer_WishList',
            new_name='CustomerWishList',
        ),
    ]