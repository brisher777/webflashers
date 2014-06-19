from django.conf.urls import patterns, include, url
from django.contrib import admin
# Examples:
# url(r'^$', 'webflashers.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('flashers.urls')),
    url(r'^cards/', include('flashers.urls')),
)
