from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, Http404

from gradebook.models import Students, Enrollments, Grades, Classes


def index(request):
	get_enrollment_list = Enrollments.objects.all().order_by('enrollmentid')[:500]
	context = {'get_enrollment_list': get_enrollment_list}
	return render(request, 'gradebook/index.html', context)

def detail(request, enrollmentid):
	try:
		enrollment = Enrollments.objects.get(pk=enrollmentid)
	except Enrollments.DoesNotExist:
		raise Http404
	return render(request, 'gradebook/detail.html', {'enrollment': enrollment})

def list_classes(request):
	get_class_id = Classes.objects.all().order_by('academicyears_academicyearid')
	context = {'get_class_id': get_class_id}
	return render(request, 'gradebook/list_classes.html', context)

# Create your views here.