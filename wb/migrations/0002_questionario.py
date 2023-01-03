# Generated by Django 4.1.4 on 2022-12-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=5)),
                ('titulo_pergunta', models.CharField(max_length=250)),
                ('pergunta', models.CharField(max_length=200)),
                ('comentario', models.CharField(max_length=200)),
            ],
        ),
    ]
