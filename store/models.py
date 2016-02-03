# -*- coding: utf-8 -*-
from django.db import models

class Group(models.Model):
    class Meta():
        db_table = 'groups'
        verbose_name = 'Группа товаров'
        verbose_name_plural = 'Группы товаров'

    group_name = models.CharField(max_length=250,null=False,verbose_name='Название группы')
    # group_goods = models.ForeignKey(Good)
    def __str__(self):
        return self.group_name

class Good(models.Model):
    class Meta():
        db_table = 'goods'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    good_name = models.CharField(max_length=250,
                                 null=False,
                                 verbose_name='Название товара')

    good_price = models.DecimalField(null=False,
                                     decimal_places=2,
                                     max_digits=10,
                                     verbose_name='Цена')

    good_description = models.TextField(blank=True,
                                        null=True,
                                        verbose_name='Подробное описание')

    good_code = models.CharField(max_length=200,
                                 null=False,
                                 verbose_name='Код товара')

    good_country = models.CharField(max_length=150,
                                    null=True,
                                    verbose_name='Страна')

    good_article = models.CharField(max_length=200,
                                    null=True,
                                    verbose_name='Артикул')

    good_size = models.CharField(max_length=200,
                                 null=True,
                                 verbose_name='Размеры')

    good_brand = models.CharField(max_length=200,
                                  null=True,
                                  verbose_name='Производитель')

    good_group = models.ForeignKey(Group, verbose_name='Группа')
    good_image = models.ImageField(upload_to='goods_img', null=True, verbose_name='Кртинка', default='goods_img/333.jpg')
    def __str__(self):
        return self.good_name

class Brand(models.Model):
    class Meta():
        db_table = 'brands'

    brand_name = models.CharField(max_length=250,null=False)
    brand_goods = models.ForeignKey(Good)

    def __str__(self):
        return self.brand_name

