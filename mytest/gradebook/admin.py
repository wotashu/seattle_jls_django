from django.contrib import admin
from gradebook.models import *
#from gradebook.models import Academicyears
#from gradebook.models import Academicquarters
#from gradebook.models import Students
#from gradebook.models import Teachers
#from gradebook.models import Enrollments
#from gradebook.models import Grades
#from gradebook.models import Assignmenttypes

def get_teacher_names(a, b):
	a = 'teacherlastname'
	b = 'teacherfirstname'
	return a, b

class Academicyearsadmin(admin.ModelAdmin):
	fields = ['academicyearid', 'academicyeartitle', 'academicyearstartdate', 'academicyearenddate']
	list_display = ('academicyearid', 'academicyeartitle', 'academicyearstartdate', 'academicyearenddate')

class Academicquartersadmin(admin.ModelAdmin):
	fields = ['academicquarterid', 'academicquartername', 'academicquarterstartdate', 'academicquarterenddate']

class EnrollmentsInline(admin.TabularInline):
	model = Enrollments
	extra = 0
	fields = ['classes_classid', 'dropstatus','attendancetotal','attendancescore']

class Studentsadmin(admin.ModelAdmin):
	fields = ['studentid', 'studentlastname', 'studentfirstname', 'studentalternativename', 'studentbirthdate']
	list_display = ('studentid', 'studentlastname', 'studentfirstname')
	search_fields = ['studentid', 'studentlastname', 'studentfirstname']
	inlines = [EnrollmentsInline]

class Teachersadmin(admin.ModelAdmin):
	fields = ['teacherid','teacherlastname', 'teacherfirstname', 'teacheremail', 'teacherphone']
	list_display = ('teacherid','teacherlastname', 'teacherfirstname')
	search_fields = ['teacherid','teacherlastname', 'teacherfirstname']

class Assignmenttypesadmin(admin.ModelAdmin):
	fields = ['assignmenttypeid', 'assignmenttitle']
	list_display = ('assignmenttypeid', 'assignmenttitle')

class Gradesadmin(admin.ModelAdmin):
	fieldsets = [
		(None,	{'fields': ['enrollments_enrollmentid', 'assignmenttypes_assignmenttypeid']}),
		('Grade', {'fields': ['gradescore'], 'classes': ['collapse']}),
	]
	list_display = ('gradeid', 'gradescore')

class Classesadmin(admin.ModelAdmin):
	fields = ['classid', 'academicyears_academicyearid', 'classsection', 'teachers_teacherid' ]
	list_display = ('classid', 'academicyears_academicyearid', 'classsection')

class GradesInline(admin.TabularInline):
	model = Grades
	extra = 0
	fields = ['assignmenttypes_assignmenttypeid', 'gradescore']

class Enrollmentsadmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['enrollmentid', 'classes_classid','students_studentid']}),
		('Attendance', {'fields': ['dropstatus','attendancetotal','attendancescore'], 'classes': ['collapse']}),
		('Notes', {'fields': ['notes'], 'classes': ['collapse']})
	]
	inlines = [GradesInline]
	list_display = ('students_studentid','classes_classid', 'dropstatus', 'notes')
	search_fields = ['notes']


admin.site.register(Academicyears, Academicyearsadmin)
admin.site.register(Academicquarters, Academicquartersadmin)
admin.site.register(Students, Studentsadmin)
admin.site.register(Teachers, Teachersadmin)
admin.site.register(Grades, Gradesadmin)
admin.site.register(Assignmenttypes, Assignmenttypesadmin)
admin.site.register(Enrollments, Enrollmentsadmin)
admin.site.register(Classes, Classesadmin)
# Register your models here.
