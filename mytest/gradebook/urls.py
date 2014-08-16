from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import TemplateView

from gradebook import views

urlpatterns = patterns('',
                       # url(r'^$', TemplateView.as_view(template_name='base.html')),
                       url(r'^$', views.index, name='index'),
                       url(r'list_classes', views.list_classes, name='list_classes'),
                       # ex: /student_id/5/
                       url(r'^(?P<enrollment_id>\d+)/$', views.detail, name='detail'),
                       url(r'homeboy', views.homeboy, name='homeboy'),
                       url(r'^students/(?P<student_id>[0-9]+)/$', views.students, name='students'),
)

urlpatterns += staticfiles_urlpatterns()