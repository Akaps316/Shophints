# Generated by Django 2.0.1 on 2018-07-22 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_featured'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured',
        ),
    ]
