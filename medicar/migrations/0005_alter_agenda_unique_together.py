# Generated by Django 4.0.6 on 2022-07-18 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicar', '0004_horario_disponivel_alter_horario_agenda_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='agenda',
            unique_together=set(),
        ),
    ]
