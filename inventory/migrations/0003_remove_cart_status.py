# Generated by Django 3.0.3 on 2020-10-19 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_product_rem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='status',
        ),
    ]