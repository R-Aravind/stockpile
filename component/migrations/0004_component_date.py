# Generated by Django 2.2 on 2019-04-15 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component', '0003_auto_20190415_0515'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
