# Generated by Django 3.0 on 2020-02-04 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0004_auto_20200204_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='annonce',
            name='photo',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]
