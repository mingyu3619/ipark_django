# Generated by Django 2.2.7 on 2021-07-02 16:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0008_memberdata_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberdata',
            name='num',
        ),
    ]