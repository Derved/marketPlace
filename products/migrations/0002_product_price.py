# Generated by Django 2.2.1 on 2019-06-01 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Precio'),
        ),
    ]