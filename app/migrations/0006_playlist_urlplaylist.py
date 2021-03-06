# Generated by Django 3.1.7 on 2022-01-08 11:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220104_1024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('titulos', models.TextField()),
                ('serie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.serie')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UrlPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('url', models.TextField()),
                ('playlist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.playlist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
