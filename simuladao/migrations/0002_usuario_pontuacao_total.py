# Generated by Django 4.0.6 on 2023-07-31 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simuladao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='pontuacao_total',
            field=models.IntegerField(default=0),
        ),
    ]