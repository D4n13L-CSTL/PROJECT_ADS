# Generated by Django 5.1.2 on 2025-04-12 14:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Head_campañas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_campañas', models.CharField(max_length=50)),
                ('fecha_creacion', models.DateField()),
                ('activa', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'Head_campanas',
            },
        ),
        migrations.CreateModel(
            name='Campañas_desc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField()),
                ('tipo_evento', models.CharField(max_length=50)),
                ('tipo_contendido', models.CharField(max_length=50)),
                ('duracion', models.IntegerField()),
                ('alcance', models.IntegerField()),
                ('inversion', models.FloatField()),
                ('head_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_campañas.head_campañas')),
            ],
            options={
                'db_table': 'Campanas_descri',
            },
        ),
    ]
