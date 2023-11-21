# Generated by Django 4.2.7 on 2023-11-20 23:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('propiedades', '0002_alter_caracteristica_options_alter_ciudad_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zona',
            name='area',
        ),
        migrations.AddField(
            model_name='zona',
            name='ciudad',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ciudad_zona', to='propiedades.ciudad'),
        ),
    ]
