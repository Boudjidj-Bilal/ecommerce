# Generated by Django 4.2.6 on 2023-11-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_taille_remove_cart_total_alter_product_taille'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='taille',
        ),
        migrations.AddField(
            model_name='product',
            name='taille',
            field=models.ManyToManyField(to='store.taille'),
        ),
    ]