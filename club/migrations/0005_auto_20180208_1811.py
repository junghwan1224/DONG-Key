# Generated by Django 2.0.1 on 2018-02-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0004_auto_20180208_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='club',
            name='position',
            field=models.IntegerField(default=2),
        ),
    ]
