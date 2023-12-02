# Generated by Django 4.2.6 on 2023-11-08 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0024_taille_tailledisponible_tailleproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tailleproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='tailleproduct',
            name='taille',
        ),
        migrations.RemoveField(
            model_name='tailleproduct',
            name='tailleDisponible',
        ),
        migrations.AddField(
            model_name='tailleproduct',
            name='product',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
        migrations.AddField(
            model_name='tailleproduct',
            name='taille',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.taille'),
        ),
        migrations.AddField(
            model_name='tailleproduct',
            name='tailleDisponible',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to='store.tailledisponible'),
        ),
    ]
