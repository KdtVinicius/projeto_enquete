# Generated by Django 4.0.6 on 2023-07-26 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simuladao', '0007_pergunta_resposta_correta_pergunta_usuario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='simulado',
        ),
    ]
