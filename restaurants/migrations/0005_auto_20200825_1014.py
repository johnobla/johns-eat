# Generated by Django 3.1 on 2020-08-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_remove_address_restaurant'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address1',
            field=models.CharField(default='', max_length=1024, verbose_name='Address line 1'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='address2',
            field=models.CharField(default='', max_length=1024, verbose_name='Address line 2'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='city',
            field=models.CharField(default='', max_length=1024, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='country',
            field=models.CharField(default='', max_length=1024, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='zip_code',
            field=models.CharField(default='', max_length=12, verbose_name='ZIP / Postal code'),
        ),
    ]
