# Generated by Django 4.1.5 on 2023-02-01 18:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_polishes_alter_polish_name'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Polishes',
        ),
        migrations.AlterModelOptions(
            name='polish',
            options={'ordering': ['brand', 'name']},
        ),
    ]
