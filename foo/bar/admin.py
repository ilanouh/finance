from django.contrib import admin

from .models import Client, Account, AccountAnalytic, Product, ProductAnalytic

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(AccountAnalytic)
admin.site.register(Product)
