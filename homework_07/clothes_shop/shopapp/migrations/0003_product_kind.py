# Generated by Django 4.0.6 on 2022-08-02 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0002_productkind'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='kind',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shopapp.productkind'),
        ),
    ]