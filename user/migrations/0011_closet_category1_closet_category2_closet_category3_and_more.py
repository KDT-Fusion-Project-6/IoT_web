# Generated by Django 4.0.4 on 2022-06-03 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_closet_closet_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='closet',
            name='category1',
            field=models.CharField(choices=[('1', '1'), ('1', '1'), ('1', '1')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='closet',
            name='category2',
            field=models.CharField(choices=[('1', '1'), ('1', '1'), ('1', '1')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='closet',
            name='category3',
            field=models.CharField(choices=[('1', '1'), ('1', '1'), ('1', '1')], default='', max_length=2),
        ),
        migrations.AddField(
            model_name='closet',
            name='category4',
            field=models.CharField(choices=[('1', '1'), ('1', '1'), ('1', '1')], default='', max_length=2),
        ),
    ]
