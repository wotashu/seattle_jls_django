from django.shortcuts import render
from django.http import Http404

from gradebook.models import Enrollments, Classes, Students, Teachers


def index(request):
    get_enrollment_list = Enrollments.objects.all().order_by('enrollment_id')[:500]
    context = {'get_enrollment_list': get_enrollment_list}
    return render(request, 'gradebook/index.html', context)


def detail(request, enrollment_id):
    try:
        enrollment = Enrollments.objects.get(pk=enrollment_id)
    except Enrollments.DoesNotExist:
        raise Http404
    return render(request, 'gradebook/detail.html', {'enrollment': enrollment})


def list_classes(request):
    get_class_id = Classes.objects.all().order_by('academic_years_academic_year_id')
    context = {'get_class_id': get_class_id}
    return render(request, 'gradebook/list_classes.html', context)


def homeboy(request):
    get_student_id = Students.objects.all()
    get_teacher_id = Teachers.objects.all()
    context_1 = {'get_student_id': get_student_id}
    context_2 = {'get_teacher_id': get_teacher_id}
    return render(request, 'gradebook/homeboy.html', context_1)
# Create your views here.