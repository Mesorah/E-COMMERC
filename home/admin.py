from django.contrib import admin

from home.models import (  # noqa E501
    Cart,
    CartItem,
    Category,
    CustomerQuestion,
    Ordered,
    Products,
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug": ('name',)
    }


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    search_fields = 'number_ordered', 'first_name', 'street_name',


@admin.register(Ordered)
class OrderedAdmin(admin.ModelAdmin):
    autocomplete_fields = 'products',


@admin.register(CustomerQuestion)
class CustomerQuestionAdmin(admin.ModelAdmin):
    pass
