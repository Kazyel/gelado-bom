# Generated by Django 4.2.5 on 2023-09-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0005_alter_picole_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acai',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='picole',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sorvete',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
