from django.conf.urls import patterns, url
from flashers import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<post_id>\d+)/$', views.detail, name='detail'),
)

