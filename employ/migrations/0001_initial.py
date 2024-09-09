# Generated by Django 5.1.1 on 2024-09-09 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('income', models.IntegerField()),
                ('description', models.CharField(max_length=255)),
                ('image_url', models.CharField(max_length=2083)),
            ],
        ),
    ]
