# Generated by Django 4.0.1 on 2022-04-02 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Stock', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stock',
            old_name='nombre',
            new_name='producto',
        ),
    ]