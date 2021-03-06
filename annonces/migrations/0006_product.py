# Generated by Django 3.0 on 2020-02-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('annonces', '0005_auto_20200204_2038'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('release_date', models.DateField()),
            ],
        ),
    ]
