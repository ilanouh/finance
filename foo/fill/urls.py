from django.conf.urls import url
from django.conf import settings

from .views import fill_clients, fill_accounts, fill_account_analytics, fill_products, fill_product_analytics, fill_product_track_record_evolution, fill_account_track_record_composition, fill_account_track_record_evolution

urlpatterns = [
    url(r'^clients/$', fill_clients, {'file': settings.BASE_DIR + '/fill/datas/ClientsTable.csv'}),
    url(r'^accounts/$', fill_accounts, {'file': settings.BASE_DIR + '/fill/datas/AccountsTable.csv'}),
    url(r'^aa/$', fill_account_analytics, {'file': settings.BASE_DIR + '/fill/datas/AccountAnalytics.csv'}),
    url(r'^products/$', fill_products, {'file': settings.BASE_DIR + '/fill/datas/ProductsTable.csv'}),
    url(r'^pa/$', fill_product_analytics, {'file': settings.BASE_DIR + '/fill/datas/ProductAnalytics.csv'}),
    url(r'^ptre/$', fill_product_track_record_evolution, {'file': settings.BASE_DIR + '/fill/datas/ProductTrackRecordEvolution.csv'}),
    url(r'^atrc/$', fill_account_track_record_composition, {'file': settings.BASE_DIR + '/fill/datas/AccountTrackRecordCompositionAmounts.csv'}),
    url(r'^atre/$', fill_account_track_record_evolution, {'file': settings.BASE_DIR + '/fill/datas/AccountTrackRecordEvolution.csv'})
]
