from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import main.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'listenlocally.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', main.views.index, name='index'),
    url(r'^db', main.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),

)
