# Generated by Django 4.2.5 on 2023-09-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_remove_acai_tamanho_remove_sorvete_tamanho'),
    ]

    operations = [
        migrations.AddField(
            model_name='acai',
            name='tamanho',
            field=models.CharField(choices=[('1 Litro', '1 Litro'), ('2 Litros', '2 Litros'), ('5 Litros', '5 Litros'), ('10 Litros', '10 Litros')], default='1 Litro', max_length=12),
        ),
    ]