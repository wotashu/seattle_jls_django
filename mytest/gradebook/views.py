from django import forms
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from gradebook.forms import AddressForm, StudentForm
from django.shortcuts import render_to_response
from django.template import RequestContext

from gradebook.models import Enrollment, Class, Student, Address


class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)


def index(request):
    get_enrollment_list = Enrollment.objects.all().order_by('enrollment_id')[:500]
    context = {'get_enrollment_list': get_enrollment_list}
    return render(request, 'gradebook/index.html', context)


def detail(request, enrollment_id):
    try:
        enrollment = Enrollment.objects.get(pk=enrollment_id)
    except Enrollment.DoesNotExist:
        raise Http404
    return render(request, 'gradebook/detail.html', {'enrollment': enrollment})


def list_classes(request):
    get_class_id = Class.objects.all().order_by('academic_years_academic_year_id')
    context = {'get_class_id': get_class_id}
    return render(request, 'gradebook/list_classes.html', context)


def homeboy(request):
    get_student_id = Student.objects.all()
    context = {'get_student_id': get_student_id}
    return render(request, 'gradebook/homeboy.html', context)


def students(request, student_id):
    try:
        student = Student.objects.get(pk=student_id)
    except Student.DoesNotExist:
        raise Http404
    context = {'student': student}
    return render(request, 'gradebook/student_id.html', context)


def add_student(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = StudentForm()
    return render_to_response('gradebook/add_student.html', {'form': form}, context)


def add_address(request):
    context = RequestContext(request)

    if request.method == 'POST':
        form = AddressForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = AddressForm()
    return render_to_response('gradebook/add_address.html', {'form': form}, context)

# Create your views here.