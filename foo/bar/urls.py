from django.conf.urls import url

from .views import IndexView, GraphView, ClientView, AccountView, SimulationView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^graph/$', GraphView.as_view(), name='graph'),
    url(r'^simulation/$', SimulationView.as_view(), name='simulation'),
    url(r'^(?P<client_id>[-\w]+)/$', ClientView.as_view(), name='client'),
    url(r'^(?P<client_id>[-\w]+)/(?P<account_id>[-\w]+)/$', AccountView.as_view(), name='account'),
]
