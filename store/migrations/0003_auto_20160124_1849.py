# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 15:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_good_good_brand'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='good',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterModelOptions(
            name='group',
            options={'verbose_name': 'Группа товаров', 'verbose_name_plural': 'Группы товаров'},
        ),
        migrations.RemoveField(
            model_name='group',
            name='group_goods',
        ),
        migrations.AddField(
            model_name='good',
            name='good_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='store.Group'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='good_article',
            field=models.CharField(max_length=200, null=True, verbose_name='Артикул'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_brand',
            field=models.CharField(max_length=200, null=True, verbose_name='Производитель'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_code',
            field=models.CharField(max_length=200, verbose_name='Код товара'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_country',
            field=models.CharField(max_length=150, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_description',
            field=models.TextField(verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_name',
            field=models.CharField(max_length=250, verbose_name='Название товара'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='good',
            name='good_size',
            field=models.CharField(max_length=200, null=True, verbose_name='Размеры'),
        ),
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=250, verbose_name='Название группы'),
        ),
    ]