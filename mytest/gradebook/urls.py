from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.views.generic.base import TemplateView
from gradebook.views import GradeDetails

from gradebook import views

urlpatterns = patterns('',
                       # url(r'^$', TemplateView.as_view(template_name='base.html')),
                       url(r'^$', views.index, name='index'),
                       url(r'^add_address/$', views.add_address, name='add_address'),
                       url(r'^add_student/$', views.add_student, name='add_student'),
                       url(r'list_classes', views.list_classes, name='list_classes'),
                       # ex: /student_id/5/
                       url(r'^(?P<enrollment_id>\d+)/$', views.detail, name='detail'),
                       url(r'student_list', views.student_list, name='student_list'),
                       url(r'^students/(?P<student_id>[0-9]+)/$', views.students, name='students'),
                       url(r'^report_card/(?P<student_id>[0-9]+)/$', views.report_card, name='report_card'),
                       url(r'^grades/(?P<slug>[-_\w]+)/$', GradeDetails.as_view(), name='grade-details'),
                       url(r'get_grades', views.grade_list, name='get-grades'),
)

urlpatterns += staticfiles_urlpatterns()