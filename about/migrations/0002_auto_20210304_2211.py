# Generated by Django 3.1.7 on 2021-03-04 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='Content',
        ),
        migrations.AddField(
            model_name='page',
            name='content',
            field=models.TextField(blank=True, max_length=254, null=True),
        ),
    ]
