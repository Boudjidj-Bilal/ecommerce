# Generated by Django 4.2.6 on 2023-10-24 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_rename_oders_cart_orders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]