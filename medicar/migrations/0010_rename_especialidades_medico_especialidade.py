# Generated by Django 4.0.6 on 2022-07-19 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicar', '0009_rename_especialidades_especialidade_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medico',
            old_name='especialidades',
            new_name='especialidade',
        ),
    ]
