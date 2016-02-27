from django.conf.urls import url

from .views import IndexView, GraphView, PersonalView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^graph/$', GraphView.as_view(), name='graph'),
    url(r'^(?P<slug>[-\w]+)/$', PersonalView.as_view(), name='personal'),
]
