# Generated by Django 4.0.4 on 2022-06-08 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_closet_outer_closet_outer_fit_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='closet_outer',
            name='category1',
            field=models.TextField(choices=[('1', '1'), ('1', '1'), ('1', '1')], default='', max_length=20),
        ),
    ]
