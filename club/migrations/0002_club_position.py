# Generated by Django 2.0.1 on 2018-02-02 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='position',
            field=models.BooleanField(default=True),
        ),
    ]
