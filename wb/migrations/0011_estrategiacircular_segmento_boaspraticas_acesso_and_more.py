# Generated by Django 4.1.4 on 2023-01-03 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0010_boaspraticas'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstrategiaCircular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estrategiacircular', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Segmento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segmento', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='boaspraticas',
            name='acesso',
            field=models.CharField(default=None, max_length=400),
        ),
        migrations.AddField(
            model_name='boaspraticas',
            name='boapratica',
            field=models.CharField(default=None, max_length=400),
        ),
        migrations.AddField(
            model_name='boaspraticas',
            name='empresa',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boaspraticas',
            name='fonte',
            field=models.CharField(default=None, max_length=200),
        ),
        migrations.AddField(
            model_name='boaspraticas',
            name='estrategiacircular',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wb.estrategiacircular'),
        ),
        migrations.AddField(
            model_name='boaspraticas',
            name='segmento',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='wb.segmento'),
        ),
    ]
