# Generated by Django 3.1.4 on 2020-12-09 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0005_auto_20201203_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cabecera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.paciente')),
                ('profesional_medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clinica.profesionalmedico')),
            ],
        ),
        migrations.AddField(
            model_name='paciente',
            name='profesionales_medicos',
            field=models.ManyToManyField(through='clinica.Cabecera', to='clinica.ProfesionalMedico'),
        ),
        migrations.AddField(
            model_name='profesionalmedico',
            name='pacientes',
            field=models.ManyToManyField(through='clinica.Cabecera', to='clinica.Paciente'),
        ),
    ]