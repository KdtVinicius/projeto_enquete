# Generated by Django 4.0.6 on 2023-07-31 01:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(verbose_name='data de cadastro de questão')),
                ('pontuacao', models.PositiveIntegerField(default=0)),
                ('usuario', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_tema', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Simulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_simulado', models.CharField(default='digite o nome do seu simulado', max_length=100)),
                ('pontuacao', models.IntegerField(default=0)),
                ('data_pub', models.DateTimeField(verbose_name='data de publicação')),
                ('data_fim', models.DateField(null=True, verbose_name='Data de encerramento')),
                ('pergunta', models.ManyToManyField(to='simuladao.pergunta')),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simuladao.tema')),
            ],
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
                ('votos_quant', models.IntegerField(default=0)),
                ('alternativa_correta', models.BooleanField(default=False)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simuladao.pergunta')),
            ],
        ),
    ]
