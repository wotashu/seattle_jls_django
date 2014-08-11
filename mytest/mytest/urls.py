from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mytest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^pdf/$', PDFTemplateView.as_view(template_name='my_template.html',
                                           filename='my_pdf.pdf'), name='pdf'),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^gradebook/', include('gradebook.urls')),
    url(r'^admin/', include(admin.site.urls)),

)


