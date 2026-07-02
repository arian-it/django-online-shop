from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/categories')

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    size = models.ManyToManyField(Size, related_name='size_products')
    color = models.ManyToManyField(Color, related_name='color_products')
    image = models.ImageField(upload_to='images/products', blank=True, null=True)
    price = models.PositiveIntegerField()
    discount = models.SmallIntegerField(default=0)


    def __str__(self):
        return f"{self.title} -- {self.description[:40]}"


