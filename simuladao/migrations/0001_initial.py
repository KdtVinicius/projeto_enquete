# Generated by Django 4.0.6 on 2023-07-04 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enunciado', models.CharField(max_length=200)),
                ('data_cadastro', models.DateTimeField(verbose_name='data de cadastro de questão')),
                ('pontuacao', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Simulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pontuacao', models.IntegerField(default=0)),
                ('data_pub', models.DateTimeField(verbose_name='data de publicação')),
                ('data_fim', models.DateField(null=True, verbose_name='Data de encerramento')),
                ('pergunta', models.ManyToManyField(to='simuladao.pergunta')),
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
                ('nome', models.CharField(max_length=100)),
                ('cpf', models.IntegerField(default=0)),
                ('simulado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simuladao.simulado')),
            ],
        ),
        migrations.AddField(
            model_name='simulado',
            name='tema',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simuladao.tema'),
        ),
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=100)),
                ('votos_quant', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simuladao.pergunta')),
            ],
        ),
    ]
