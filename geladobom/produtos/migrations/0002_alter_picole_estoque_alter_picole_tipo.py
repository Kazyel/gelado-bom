# Generated by Django 4.2.5 on 2023-09-25 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picole',
            name='estoque',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='picole',
            name='tipo',
            field=models.CharField(choices=[('Cobertura', 'Cobertura'), ('Normal', 'Normal')], default='Normal', max_length=9),
        ),
    ]
