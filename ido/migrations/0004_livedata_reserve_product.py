# Generated by Django 3.1.7 on 2021-02-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0003_auto_20210219_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='livedata',
            name='reserve_product',
            field=models.CharField(default='', max_length=10),
        ),
    ]
