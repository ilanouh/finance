from django.contrib import admin

from .models import Client, Account, AccountAnalytic, Product, ProductAnalytic, ProductTrackRecordEvolution, AccountTrackRecordComposition, AccountTrackRecordEvolution

admin.site.register(Client)
admin.site.register(Account)
admin.site.register(AccountAnalytic)
admin.site.register(Product)
admin.site.register(ProductAnalytic)
admin.site.register(ProductTrackRecordEvolution)
admin.site.register(AccountTrackRecordComposition)
admin.site.register(AccountTrackRecordEvolution)
