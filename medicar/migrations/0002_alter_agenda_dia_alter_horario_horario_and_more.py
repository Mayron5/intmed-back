# Generated by Django 4.0.6 on 2022-07-18 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='dia',
            field=models.DateField(max_length=10),
        ),
        migrations.AlterField(
            model_name='horario',
            name='horario',
            field=models.TimeField(max_length=6),
        ),
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together={('medico', 'dia')},
        ),
        migrations.AlterUniqueTogether(
            name='horario',
            unique_together={('horario', 'agenda')},
        ),
    ]
