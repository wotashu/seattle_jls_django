from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^gradebook/', include('gradebook.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
