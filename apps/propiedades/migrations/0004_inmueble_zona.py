# Generated by Django 4.2.7 on 2023-11-20 23:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0003_remove_zona_area_zona_ciudad'),
    ]

    operations = [
        migrations.AddField(
            model_name='inmueble',
            name='zona',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='propiedades.zona'),
        ),
    ]
