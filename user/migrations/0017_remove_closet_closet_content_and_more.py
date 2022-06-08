# Generated by Django 4.0.4 on 2022-06-07 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_alter_closet_onepiece_closet_onepiece_uploadedfile_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='closet',
            name='closet_content',
        ),
        migrations.AlterField(
            model_name='closet',
            name='closet_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='closet',
            name='closet_url',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='closet_onepiece',
            name='closet_onepiece_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='closet_onepiece',
            name='closet_onepiece_url',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='closet_outer',
            name='closet_outer_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='closet_outer',
            name='closet_outer_url',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='closet_pants',
            name='closet_pants_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='closet_pants',
            name='closet_pants_url',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='closet_top',
            name='closet_top_title',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='closet_top',
            name='closet_top_url',
            field=models.CharField(default='', max_length=50),
        ),
    ]
