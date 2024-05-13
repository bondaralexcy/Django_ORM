from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Category(models.Model):
    category_name = models.CharField(max_length=100, verbose_name='Наименование')
    descr = models.CharField(max_length=500, verbose_name='Описание')

    def __str__(self):
        return f'{self.category_name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('category_name',)


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Наименование')
    descr = models.CharField(max_length=500, verbose_name='Описание')
    preview = models.ImageField(upload_to='products/', verbose_name='Изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена за покупку')
    created_at = models.DateTimeField(verbose_name='Дата создания ')
    updated_at = models.DateTimeField(verbose_name='Дата последнего изменения')
    manufactured_at = models.DateTimeField(verbose_name='Дата производства продукта', **NULLABLE)

    def __str__(self):
        return f'{self.product_name} {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)
