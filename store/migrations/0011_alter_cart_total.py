# Generated by Django 4.2.6 on 2023-10-25 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_order_prixorder'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='total',
            field=models.IntegerField(default=0),
        ),
    ]
