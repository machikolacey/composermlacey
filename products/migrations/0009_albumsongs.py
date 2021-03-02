# Generated by Django 3.1.7 on 2021-03-02 23:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_album'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumSongs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.TextField(blank=True, max_length=250, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.album')),
            ],
        ),
    ]
