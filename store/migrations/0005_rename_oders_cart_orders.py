# Generated by Django 4.2.6 on 2023-10-24 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_cart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='oders',
            new_name='orders',
        ),
    ]
