# Generated by Django 3.1.7 on 2022-02-03 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_channel_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='episodio',
            name='selected',
            field=models.BooleanField(default=False),
        ),
    ]
