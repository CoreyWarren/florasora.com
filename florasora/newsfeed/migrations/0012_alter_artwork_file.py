# Generated by Django 4.0.3 on 2022-06-03 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0011_alter_artwork_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='file',
            field=models.ImageField(upload_to='artworks/'),
        ),
    ]