# Generated by Django 4.0.4 on 2022-06-02 21:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0008_alter_artwork_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artwork',
            options={'ordering': ['date_post']},
        ),
    ]
