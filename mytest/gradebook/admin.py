from django.contrib import admin
from gradebook.models import AcademicYears
from gradebook.models import AcademicQuarters
from gradebook.models import Students
from gradebook.models import Teachers
from gradebook.models import Enrollments
from gradebook.models import Grades
from gradebook.models import AssignmentTypes
from gradebook.models import Classes


class AcademicYearsAdmin(admin.ModelAdmin):
    fields = ['academic_year_id', 'academic_year_title', 'academic_year_start_date', 'academic_year_end_date']
    list_display = ('academic_year_id', 'academic_year_title', 'academic_year_start_date', 'academic_year_end_date')


class AcademicQuartersAdmin(admin.ModelAdmin):
    fields = ['academic_quarter_id', 'academic_quarter_name', 'academic_quarter_start_date',
              'academic_quarter_end_date']


class EnrollmentsInline(admin.TabularInline):
    model = Enrollments
    extra = 0
    fields = ['classes_class_id', 'drop_status', 'attendance_total', 'attendance_score']


class StudentsAdmin(admin.ModelAdmin):
    fields = ['student_id', 'student_last_name', 'student_first_name', 'student_alternative_name', 'student_birth_date']
    list_display = ('student_id', 'student_last_name', 'student_first_name', 'student_birth_date')
    search_fields = ['student_id', 'student_last_name', 'student_first_name']
    inlines = [EnrollmentsInline]


class TeachersAdmin(admin.ModelAdmin):
    fields = ['teacher_id', 'teacher_last_name', 'teacher_first_name', 'teacher_email', 'teacher_phone']
    list_display = ('teacher_id', 'teacher_last_name', 'teacher_first_name')
    search_fields = ['teacher_id', 'teacher_last_name', 'teacher_first_name']


class AssignmentTypesAdmin(admin.ModelAdmin):
    fields = ['assignment_type_id', 'assignment_title']
    list_display = ('assignment_type_id', 'assignment_title')


class GradesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['enrollments_enrollment_id', 'assignment_types_assignment_type_id']}),
        ('Grade', {'fields': ['grade_score'], 'classes': ['collapse']}),
    ]
    list_display = ('grade_id', 'grade_score')


class ClassesAdmin(admin.ModelAdmin):
    fields = ['class_id', 'academic_years_academic_year_id', 'class_section', 'teachers_teacher_id']
    list_display = ('class_id', 'academic_years_academic_year_id', 'class_section')


class GradesInline(admin.TabularInline):
    model = Grades
    extra = 0
    fields = ['assignment_types_assignment_type_id', 'grade_score']


class EnrollmentsAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['enrollment_id', 'classes_class_id', 'students_student_id']}),
        ('Attendance', {'fields': ['drop_status', 'attendance_total', 'attendance_score'], 'classes': ['collapse']}),
        ('Notes', {'fields': ['notes'], 'classes': ['collapse']})
    ]
    inlines = [GradesInline]
    list_display = ('students_student_id', 'classes_class_id', 'drop_status', 'notes')
    search_fields = ['students_student_id__student_last_name', 'students_student_id__student_first_name', 'notes']


admin.site.register(AcademicYears, AcademicYearsAdmin)
admin.site.register(AcademicQuarters, AcademicQuartersAdmin)
admin.site.register(Students, StudentsAdmin)
admin.site.register(Teachers, TeachersAdmin)
admin.site.register(Grades, GradesAdmin)
admin.site.register(AssignmentTypes, AssignmentTypesAdmin)
admin.site.register(Enrollments, EnrollmentsAdmin)
admin.site.register(Classes, ClassesAdmin)
# Register your models here.
