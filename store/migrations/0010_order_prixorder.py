# Generated by Django 4.2.6 on 2023-10-25 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_cart_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='prixOrder',
            field=models.IntegerField(default=0),
        ),
    ]
