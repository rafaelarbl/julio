# Generated by Django 4.1.4 on 2023-01-03 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wb', '0019_boaspraticas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='boaspraticas',
            name='estrategiacircular',
        ),
        migrations.RemoveField(
            model_name='boaspraticas',
            name='segmento',
        ),
        migrations.DeleteModel(
            name='EstrategiaCircular',
        ),
        migrations.DeleteModel(
            name='Segmento',
        ),
    ]