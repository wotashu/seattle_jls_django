from django.contrib import admin
from gradebook.models import Academicyears
from gradebook.models import Academicquarters
from gradebook.models import Students
from gradebook.models import Teachers
from gradebook.models import Grades
from gradebook.models import Assignmenttypes

class Academicyearsadmin(admin.ModelAdmin):
	fields = ['academicyearid', 'academicyeartitle', 'academicyearstartdate', 'academicyearenddate']
	list_display = ('academicyearid', 'academicyeartitle', 'academicyearstartdate', 'academicyearenddate')

class Academicquartersadmin(admin.ModelAdmin):
	fields = ['academicquarterid', 'academicquartername', 'academicquarterstartdate', 'academicquarterenddate']

class Studentsadmin(admin.ModelAdmin):
	fields = ['studentid', 'studentlastname', 'studentfirstname', 'studentalternativename', 'studentbirthdate']
	list_display = ('studentid', 'studentlastname', 'studentfirstname')
	search_fields = ['studentid', 'studentlastname', 'studentfirstname']

class Teachersadmin(admin.ModelAdmin):
	fields = ['teacherid','teacherlastname', 'teacherfirstname', 'teacheremail', 'teacherphone']
	list_display = ('teacherid','teacherlastname', 'teacherfirstname')
	search_fields = ['teacherid','teacherlastname', 'teacherfirstname']


class Gradesadmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields': ['enrollments_enrollmentid']}),
		('Grade', {'fields': ['gradescore'], 'classes': ['collapse']}),
	]
	list_display = ('enrollments_enrollmentid', 'assignmenttypes_assignmenttypeid', 'gradescore')

class Assignmenttypesadmin(admin.ModelAdmin):
	fields = ['assignmenttypeid', 'assignmenttitle']
	list_display = ('assignmenttypeid', 'assignmenttitle')



admin.site.register(Academicyears, Academicyearsadmin)
admin.site.register(Academicquarters, Academicquartersadmin)
admin.site.register(Students, Studentsadmin)
admin.site.register(Teachers, Teachersadmin)
admin.site.register(Grades, Gradesadmin)
admin.site.register(Assignmenttypes, Assignmenttypesadmin)
# Register your models here.
