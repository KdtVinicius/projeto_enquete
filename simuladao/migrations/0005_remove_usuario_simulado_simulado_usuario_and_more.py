# Generated by Django 4.0.6 on 2023-07-06 12:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simuladao', '0004_alter_simulado_nome_simulado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='simulado',
        ),
        migrations.AddField(
            model_name='simulado',
            name='usuario',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='simuladao.usuario'),
        ),
        migrations.AlterField(
            model_name='simulado',
            name='nome_simulado',
            field=models.CharField(default='', max_length=100),
        ),
    ]
