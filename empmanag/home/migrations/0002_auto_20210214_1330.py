# Generated by Django 3.1.5 on 2021-02-14 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='post',
            field=models.CharField(max_length=30),
        ),
    ]
