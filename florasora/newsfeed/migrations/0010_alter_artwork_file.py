# Generated by Django 4.0.4 on 2022-06-02 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0009_alter_artwork_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='file',
            field=models.ImageField(upload_to='C:/artworks_db/artworks/'),
        ),
    ]
