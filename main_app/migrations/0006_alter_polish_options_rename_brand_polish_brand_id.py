# Generated by Django 4.1.5 on 2023-01-29 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_rename_polishes_polish'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='polish',
            options={'ordering': ['brand_id', 'name']},
        ),
        migrations.RenameField(
            model_name='polish',
            old_name='brand',
            new_name='brand_id',
        ),
    ]
