# Generated by Django 5.0.6 on 2024-05-25 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='cuantity',
            new_name='quantity',
        ),
    ]