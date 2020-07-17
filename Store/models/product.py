from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=2)
    description = models.CharField(
        max_length=280, default="", blank=True, null=True)
    image = models.ImageField(upload_to="uploads/products/")

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_id(category_id):
        if (category_id):
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_products_by_id(product_ids):
        return Product.objects.filter(id__in=product_ids)
