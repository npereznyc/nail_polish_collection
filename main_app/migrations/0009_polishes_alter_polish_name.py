# Generated by Django 4.1.5 on 2023-01-29 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_delete_polishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Polishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=400)),
                ('brand', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['brand', 'name'],
            },
        ),
        migrations.AlterField(
            model_name='polish',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]