# Generated by Django 3.1.7 on 2021-03-02 23:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='products.product'),
        ),
    ]
