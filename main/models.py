from django.db import models, connection

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование категории",
    )
    descr = models.CharField(
        max_length=500,
        verbose_name="Описание",
        **NULLABLE,
    )


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = [
            "category_name",
        ]


    @classmethod
    def truncate_table_restart_id(cls):
        """ Метод очистки таблицы со сбросом автоинкремента счетчика
        Спасибо, Владислав Печеневский"""
        with connection.cursor() as cursor:
            cursor.execute(f'TRUNCATE TABLE {cls._meta.db_table} RESTART IDENTITY CASCADE')

    def __str__(self):
        return f"{self.category_name}"

class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите наименование продукта",
    )
    descr = models.CharField(
        max_length=500,
        verbose_name="Описание",
    )
    preview = models.ImageField(
        upload_to="main/products/",
        verbose_name="Изображение",
        **NULLABLE,
    )
    category = models.ForeignKey(
        "Category",
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку",
    )
    created_at = models.DateTimeField(
        verbose_name="Дата создания", auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name="Дата последнего изменения", auto_now=True,
    )

    def __str__(self):
        return f"{self.product_name} {self.price}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = [
            "product_name",
        ]
