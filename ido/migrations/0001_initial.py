# Generated by Django 3.1.6 on 2021-02-15 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='covidRecord',
            fields=[
                ('name', models.CharField(default='', max_length=20)),
                ('major', models.CharField(default='', max_length=20)),
                ('student_num', models.CharField(default='', max_length=20)),
                ('phone_num', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('enter_time', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='excelDB',
            fields=[
                ('name', models.CharField(default='', max_length=20)),
                ('major', models.CharField(default='', max_length=20)),
                ('student_num', models.CharField(default='', max_length=20)),
                ('phone_num', models.CharField(default='', max_length=15, null=True)),
                ('reserve_date', models.CharField(default='', max_length=20)),
                ('reserve_product', models.CharField(default='', max_length=10)),
                ('email', models.CharField(default='', max_length=128, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='pastUser',
            fields=[
                ('name', models.CharField(default='', max_length=20)),
                ('major', models.CharField(default='', max_length=20)),
                ('student_num', models.CharField(default='', max_length=20)),
                ('phone_num', models.CharField(default='', max_length=15, primary_key=True, serialize=False)),
                ('reserve_date', models.CharField(default='', max_length=20)),
                ('reserve_product', models.CharField(default='', max_length=20)),
                ('email', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('name', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('major', models.CharField(blank=True, default='', max_length=20, null=True)),
                ('student_num', models.CharField(max_length=50)),
                ('phone_num', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('enter_time', models.CharField(default='', max_length=50, null=True)),
            ],
        ),
    ]
