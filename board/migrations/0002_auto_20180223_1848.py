# Generated by Django 2.0.2 on 2018-02-23 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0010_auto_20180214_1146'),
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tag',
        ),
        migrations.AddField(
            model_name='article',
            name='club',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='club.Club'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
