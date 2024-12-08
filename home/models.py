from django.db import models
from django.conf import settings


class Products(models.Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    cover = models.ImageField(
        upload_to='products/%Y/%m/%d/',
        blank=True, null=True,
        default='default/image_default.png'
    )
    name = models.CharField(max_length=55)
    price = models.IntegerField()
    description = models.TextField(null=True)
    stock = models.IntegerField(null=True)  # colocar positiveinteger
    is_published = models.BooleanField(null=True, default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name}'


class Cart(models.Model):
    products = models.ManyToManyField(Products)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='cart'  # user.cart  Retorna o carrinho
                             # associado ao usuário
    )

    def __str__(self):
        return f'Carrinho do {self.user}'
