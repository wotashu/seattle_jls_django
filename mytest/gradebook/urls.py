from django.conf.urls import patterns, url

from gradebook import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'list_classes', views.list_classes, name='list_classes'),
    # ex: /student_id/5/
    url(r'^(?P<enrollment_id>\d+)/$', views.detail, name='detail'),
    url(r'homeboy', views.homeboy, name='homeboy'),
    url(r'^students/(?P<student_id>[0-9]+)/$', views.students, name='students'),
)