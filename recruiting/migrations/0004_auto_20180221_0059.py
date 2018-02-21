# Generated by Django 2.0.1 on 2018-02-20 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0003_auto_20180216_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='long_answer',
            field=models.TextField(blank=True, null=True, verbose_name='항목 답변 내용'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='short_answer',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='질문 답변 내용'),
        ),
        migrations.AlterField(
            model_name='applicantresume',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='지원서 사진'),
        ),
    ]
