# Generated by Django 4.0.4 on 2022-06-10 20:06

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='codi_clothes',
            fields=[
                ('cId', models.IntegerField(primary_key=True, serialize=False)),
                ('codiId', models.IntegerField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Musinsa_Closet',
            fields=[
                ('clothesId', models.IntegerField(primary_key=True, serialize=False)),
                ('closet_title', models.CharField(default='', max_length=200)),
                ('imgUrl', models.CharField(default='', max_length=50)),
                ('mainCategory', models.TextField(choices=[(1, 'Top'), (2, 'Pants'), (3, 'Outer'), (4, 'Onepiece')], default='', max_length=20)),
                ('outer', models.TextField(choices=[(0, 'no'), (1, 'Coat'), (2, 'Jacket'), (3, 'Jumper'), (4, 'Padding'), (5, 'Best'), (6, 'Cardigan '), (7, 'Zip-Up')], default='0', max_length=20)),
                ('top', models.TextField(choices=[(0, 'no'), (1, 'Blouse'), (2, 'T-shirt'), (3, 'Knit'), (4, 'Hoodie')], default='0', max_length=20)),
                ('pants', models.TextField(choices=[(0, 'no'), (1, 'Blue jeans'), (2, 'Pants'), (3, 'Skirt'), (4, 'Leggings'), (5, 'Jogger pants')], default='0', max_length=20)),
                ('onepiece', models.TextField(choices=[(0, 'no'), (1, 'onepiece'), (2, 'twopiece')], default='0', max_length=20)),
                ('closet_style', models.CharField(default='', max_length=100)),
                ('closet_color', models.CharField(default='', max_length=100)),
                ('barndName', models.CharField(default='', max_length=50)),
                ('ragisterDate', models.DateTimeField(default='', max_length=200)),
                ('spring', models.BooleanField(default=True)),
                ('summer', models.BooleanField(default=True)),
                ('autumn', models.BooleanField(default=True)),
                ('windter', models.BooleanField(default=True)),
                ('elasticity', models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('transparency', models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('thickness', models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('texture', models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('price', models.IntegerField(default=1, null=True)),
                ('regDate', models.DateField(verbose_name=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='preferences',
            fields=[
                ('preferences_id1', models.IntegerField(primary_key=True, serialize=False)),
                ('ratingDate', models.DateField(verbose_name=datetime.datetime.now)),
                ('preferences_id2', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Closet_onepiece',
        ),
        migrations.DeleteModel(
            name='Closet_outer',
        ),
        migrations.DeleteModel(
            name='Closet_pants',
        ),
        migrations.DeleteModel(
            name='Closet_top',
        ),
        migrations.AddField(
            model_name='closet',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_color',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_fall',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_fit',
            field=models.IntegerField(default=1, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_spring',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_style',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_summer',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='closet_winter',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='closet',
            name='onepiece',
            field=models.TextField(choices=[(0, 'no'), (1, 'onepiece'), (2, 'twopiece')], default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='outer',
            field=models.TextField(choices=[(0, 'no'), (1, 'Coat'), (2, 'Jacket'), (3, 'Jumper'), (4, 'Padding'), (5, 'Best'), (6, 'Cardigan '), (7, 'Zip-Up')], default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='pants',
            field=models.TextField(choices=[(0, 'no'), (1, 'Blue jeans'), (2, 'Pants'), (3, 'Skirt'), (4, 'Leggings'), (5, 'Jogger pants')], default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='section',
            field=models.TextField(choices=[(1, 'Top'), (2, 'Pants'), (3, 'Outer'), (4, 'Onepiece')], default='', max_length=20),
        ),
        migrations.AddField(
            model_name='closet',
            name='top',
            field=models.TextField(choices=[(0, 'no'), (1, 'Blouse'), (2, 'T-shirt'), (3, 'Knit'), (4, 'Hoodie')], default='0', max_length=20),
        ),
        migrations.CreateModel(
            name='codi',
            fields=[
                ('codiId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='user.codi_clothes')),
                ('coditype', models.CharField(default='', max_length=10)),
                ('registerDate', models.DateField(verbose_name=datetime.datetime.now)),
            ],
        ),
        migrations.AddField(
            model_name='codi_clothes',
            name='clothesId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.musinsa_closet'),
        ),
        migrations.AddField(
            model_name='preferences',
            name='codiId',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.codi'),
        ),
    ]