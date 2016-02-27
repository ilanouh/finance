from django.conf.urls import url

from .views import IndexView, GraphView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^graph/$', GraphView.as_view(), name='graph'),
]
