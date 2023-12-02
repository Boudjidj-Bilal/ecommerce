# Generated by Django 4.2.6 on 2023-11-06 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_product_taille_delete_taille'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taille',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taille', models.CharField(max_length=32)),
                ('tailleDisponible', models.BooleanField(default=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='taille',
            field=models.ManyToManyField(to='store.taille'),
        ),
    ]