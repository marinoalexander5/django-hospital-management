# Generated by Django 3.1.4 on 2020-12-03 19:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_auto_20201203_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='historial_medico',
        ),
        migrations.AddField(
            model_name='historialmedico',
            name='paciente',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='clinica.paciente'),
        ),
    ]
