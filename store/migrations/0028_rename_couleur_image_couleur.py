# Generated by Django 4.2.6 on 2023-11-25 10:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0027_article_categorie_couleur_produit_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Couleur',
            new_name='Image_Couleur',
        ),
    ]
