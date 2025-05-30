# Generated by Django 5.1.7 on 2025-05-09 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_pautasMaker', '0001_initial'),
        ('app_perfiles', '0007_header_modelos_numero_tlf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pautas',
            name='autorizacio_comercial',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pautas',
            name='autorizacion_directiva',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pautas',
            name='modelo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pautas_asignadas', to='app_perfiles.header_modelos'),
        ),
    ]
