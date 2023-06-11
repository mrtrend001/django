from django.db import models


# Customer Tag Product Order
class CustomerCL(models.Model):
    name = models.CharField("Введите ваше имя?", max_length=20)
    phone = models.CharField("Ваш номер телефона?", default="+996", max_length=15)
    email = models.EmailField("Ваш email", blank=True)

    def __str__(self):
        return self.name


class TagCL(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCL(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    name = models.CharField("Введите название товара", max_length=100)
    price = models.PositiveIntegerField("Цена товара?", default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    tag = models.ManyToManyField(TagCL, verbose_name="tag_list", null=True)

    def __str__(self):
        return self.name


class OrderCL(models.Model):
    STATUS = (
        ("На ожидании", "На ожидании"),
        ("В пути", "В пути"),
        ("Доставлен", "Доставлен"),
    )
    customer = models.ForeignKey(CustomerCL, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductCL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUS)

    def __str__(self):
        return self.status
