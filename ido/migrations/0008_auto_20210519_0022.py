# Generated by Django 3.1.7 on 2021-05-19 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ido', '0007_auto_20210519_0021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livedata',
            name='email',
        ),
        migrations.AlterField(
            model_name='livedata',
            name='phone_num',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
        ),
    ]
