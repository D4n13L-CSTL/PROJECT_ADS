# Generated by Django 5.1.7 on 2025-05-15 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Publicidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificacion', models.DateTimeField(auto_now=True, null=True)),
                ('activa', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Publicidad',
            },
        ),
        migrations.CreateModel(
            name='Items_presupuesto_publicidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_item', models.CharField(blank=True, max_length=50, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('monto_item', models.CharField(blank=True, max_length=50, null=True)),
                ('id_publicidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_publicidades.publicidad')),
            ],
            options={
                'db_table': 'Items_presupuesto_publicidades',
            },
        ),
    ]
