# Generated by Django 4.2.6 on 2023-10-25 16:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_product_taille'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
    ]
