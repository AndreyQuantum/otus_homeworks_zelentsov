# Generated by Django 4.0.6 on 2022-08-02 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_size_product_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='size',
            name='eu',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='size',
            name='jpn',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='size',
            name='usa',
            field=models.CharField(max_length=3, null=True, unique=True),
        ),
    ]
