# Generated by Django 4.0.6 on 2023-07-05 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simuladao', '0003_alter_simulado_nome_simulado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='simulado',
            name='nome_simulado',
            field=models.CharField(default='digite o nome do seu simulado', max_length=100),
        ),
    ]
