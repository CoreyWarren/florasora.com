# Generated by Django 4.0.4 on 2022-05-27 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsfeed', '0002_artwork'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]