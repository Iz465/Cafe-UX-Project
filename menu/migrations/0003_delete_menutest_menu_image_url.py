# Generated by Django 5.1.1 on 2024-10-03 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_menutest'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Menutest',
        ),
        migrations.AddField(
            model_name='menu',
            name='image_url',
            field=models.CharField(default='https://static.vecteezy.com/system/resources/previews/009/726/151/non_2x/pixel-art-coffee-cup-icon-for-8bit-game-on-white-background-vector.jpg', max_length=255),
            preserve_default=False,
        ),
    ]
