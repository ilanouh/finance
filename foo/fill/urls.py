from django.conf.urls import url

from .views import fill_clients, fill_accounts, fill_account_analytics, fill_products, fill_product_analytics, fill_product_track_record_evolution, fill_account_track_record_composition, fill_account_track_record_evolution

urlpatterns = [
    url(r'^clients/$', fill_clients, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/ClientsTable.csv'}),
    url(r'^accounts/$', fill_accounts, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/AccountsTable.csv'}),
    url(r'^accountanalytics/$', fill_account_analytics, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/AccountAnalytics.csv'}),
    url(r'^products/$', fill_products, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/ProductsTable.csv'}),
    url(r'^productanalytics/$', fill_product_analytics, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/ProductsAnalytics.csv'}),
    url(r'^producttrackrecordevolution/$', fill_product_track_record_evolution, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/ProductsTrackRecordEvolution.csv'}),
    url(r'^accounttrackrecordcomposition/$', fill_account_track_record_composition, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/AccountTrackRecordComposition.csv'}),
    url(r'^accounttrackrecordevolution/$', fill_account_track_record_evolution, {'file': '/nfs/2013/i/ibuchwal/Downloads/Atelier/Data/AccountTrackRecordEvolution.csv'})
]
