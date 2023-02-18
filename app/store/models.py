from django.db import models


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.CharField(max_length=300, null=True, blank=False, verbose_name="Описание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование")
    description = models.CharField(max_length=300, null=True, blank=False, verbose_name="Описание")
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Стоимость")
    image = models.CharField(max_length=300, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.category} - {self.title}"

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
