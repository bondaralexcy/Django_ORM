from django.contrib import admin
from main.models import Category, Product
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'category_name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'product_name', 'price', 'category', 'descr')
    # Добавляем поля для фильтрации
    list_filter = ('category',)

    # Добавляем поля для поиска
    search_fields = ('product_name', 'descr',)
