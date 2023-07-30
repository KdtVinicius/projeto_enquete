# Generated by Django 4.0.6 on 2023-07-26 20:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simuladao', '0006_remove_simulado_usuario_usuario_simulado_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pergunta',
            name='resposta_correta',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='pergunta',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='pergunta',
            name='pontuacao',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='simulado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simuladao.simulado'),
        ),
    ]