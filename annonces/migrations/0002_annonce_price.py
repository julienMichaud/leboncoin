# Generated by Django 3.0 on 2020-02-01 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
