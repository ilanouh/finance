from django.conf.urls import url

from .views import fill_clients, fill_accounts, fill_account_analytics, fill_products

urlpatterns = [
    url(r'^clients/$', fill_clients, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/ClientsTable.csv'}),
    url(r'^accounts/$', fill_accounts, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/AccountsTable.csv'}),
    url(r'^accountanalytics/$', fill_account_analytics, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/AccountAnalytics.csv'}),
    url(r'^products/$', fill_products, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/ProductsTable.csv'}),
]
