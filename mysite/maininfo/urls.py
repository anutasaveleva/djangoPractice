from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.mainPage, name='main'),
    url(r'^question/$', views.questionPage, name='questions'),
    url(r'^question/([0-9]+)/$', views.detail, name='detail'),
url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
url(r'^ithink/$', views.opinionPage, name='opinions'),
url(r'^iwish/$', views.wishPage, name='wishes'),
]