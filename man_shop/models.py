from django.db import models


class Surv(models.Model):
    BRANCH = (
        ('ТРЦ "АЗИЯ МОЛЛ', 'ТРЦ "АЗИЯ МОЛЛ'),
        ('Дордой Плаза 1. 1-этаж, бутикD2 ', 'Дордой Плаза 1. 1-этаж, бутикD2 ')
    )
    AVAILABILITY = (
        ('Да', 'Да'),
        ('Нет', 'Нет')
    )

    name = models.TextField()
    image = models.ImageField(upload_to='')
    compound = models.TextField()
    size = models.TextField('Размер', max_length=4)
    manufacturer = models.TextField('Производитель')
    availability = models.CharField('Есть ли в наличии?', max_length=3, choices=AVAILABILITY)
    which_branch = models.TextField('В каком филиале', choices=BRANCH)
    created_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    name_reviews = models.ForeignKey(Surv, on_delete=models.CASCADE,
                                     related_name='comment_object')
    description = models.TextField('your reviews')
    create_ad = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
