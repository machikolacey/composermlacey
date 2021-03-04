# Generated by Django 3.1.7 on 2021-03-04 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_auto_20210304_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='SampleVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=254)),
                ('subtitle', models.CharField(max_length=254)),
                ('embed', models.TextField(blank=True, null=True)),
                ('details', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
