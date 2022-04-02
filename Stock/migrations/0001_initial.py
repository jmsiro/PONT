# Generated by Django 4.0.1 on 2022-04-02 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rubro', models.CharField(max_length=80)),
                ('subrubro', models.CharField(max_length=80)),
                ('nombre', models.CharField(max_length=80)),
                ('unidad', models.CharField(max_length=8)),
                ('cantidad', models.CharField(max_length=8)),
                ('costo', models.CharField(max_length=8)),
                ('ultima_compra', models.DateTimeField()),
            ],
        ),
    ]
