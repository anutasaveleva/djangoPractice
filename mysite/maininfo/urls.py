from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.mainPage, name='main'),
    url('(?P<id>[0-9]+)/$', views.detail, name='detail')
]