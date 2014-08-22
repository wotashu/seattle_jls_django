from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from gradebook.models import AcademicYear, AcademicQuarter, Student, Teacher
from gradebook.models import Enrollment, Grade, AssignmentType, Class, Address, Room, Curriculum


class ClassesInline(admin.TabularInline):
    model = Class
    extra = 0
    fields = ['academic_quarters_academic_quarter_id', 'courses_course_id', 'class_section', 'teachers_teacher_id']


class AcademicYearsAdmin(admin.ModelAdmin):
    fields = ['academic_year_id', 'academic_year_title', 'academic_year_start_date', 'academic_year_end_date']
    list_display = ('academic_year_id', 'academic_year_title', 'academic_year_start_date', 'academic_year_end_date')
    inlines = [ClassesInline]


class AcademicQuartersAdmin(admin.ModelAdmin):
    fields = ['academic_quarter_id', 'academic_quarter_name', 'academic_quarter_start_date',
              'academic_quarter_end_date']


class EnrollmentsInline(admin.TabularInline):
    model = Enrollment
    extra = 0
    fields = ['classes_class_id', 'drop_status', 'attendance_total', 'attendance_score']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    }


class StudentsAdmin(admin.ModelAdmin):
    fields = ['student_id', 'student_last_name', 'student_first_name', 'student_alternative_name', 'student_birth_date']
    list_display = ('student_id', 'student_last_name', 'student_first_name', 'student_birth_date')
    search_fields = ['student_id', 'student_last_name', 'student_first_name']
    inlines = [EnrollmentsInline]
    readonly_fields = ('student_id',)


class TeachersAdmin(admin.ModelAdmin):
    fields = ['teacher_id', 'teacher_last_name', 'teacher_first_name', 'teacher_email', 'teacher_phone']
    list_display = ('teacher_id', 'teacher_last_name', 'teacher_first_name')
    search_fields = ['teacher_id', 'teacher_last_name', 'teacher_first_name']
    readonly_fields = ('teacher_id',)


class AssignmentTypesAdmin(admin.ModelAdmin):
    fields = ['assignment_type_id', 'assignment_title']
    list_display = ('assignment_type_id', 'assignment_title')


class GradesAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['enrollments_enrollment_id', 'assignment_types_assignment_type_id']}),
        ('Grade', {'fields': ['grade_score'], 'classes': ['collapse']}),
    ]
    list_display = ('grade_id', 'grade_score')


class StudentEnrollmentInline(admin.TabularInline):
    readonly_fields = ['self_link', ]
    model = Enrollment
    extra = 1
    # fk_name = "classes_class_id"
    fields = ['students_student_id', 'drop_status', 'attendance_total', 'attendance_score', 'notes', 'self_link']
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    }


class ClassesAdmin(admin.ModelAdmin):
    fields = ['class_id', 'academic_years_academic_year_id', 'courses_course_id', 'class_section',
              'teachers_teacher_id']
    list_display = ('class_id', 'academic_years_academic_year_id', 'academic_quarters_academic_quarter_id',
                    'courses_course_id', 'class_section', 'teachers_teacher_id')
    search_fields = ['academic_quarters_academic_quarter_id__academic_quarter_name',
                     'academic_years_academic_year_id__academic_year_id',
                     'academic_years_academic_year_id__academic_year_title', 'courses_course_id__course_level',
                     'teachers_teacher_id__teacher_last_name', 'teachers_teacher_id__teacher_first_name']
    inlines = [StudentEnrollmentInline]
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '40'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    }
    readonly_fields = ('class_id',)


class GradesInline(admin.TabularInline):
    model = Grade
    extra = 1
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
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size': '20'})},
        models.TextField: {'widget': Textarea(attrs={'rows': 2, 'cols': 40})},
    }
    readonly_fields = ('enrollment_id',)


class AddressAdmin(admin.ModelAdmin):
    fields = ['address_id', 'address_street_1', 'address_street_2', 'address_city', 'address_state', 'address_zip',
              'address_country']
    search_fields = ['address_street_1', 'address_street_2', 'address_city', 'address_state', 'address_zip',
                     'address_country']
    list_display = ('address_street_1', 'address_street_2', 'address_city', 'address_state', 'address_zip',
                    'address_country')
    readonly_fields = ('address_id',)


class RoomAdmin(admin.ModelAdmin):
    fields = ['room_id', 'building', 'capacity', 'equipment']
    readonly_fields = ('room_id',)


class CurriculumAdmin(admin.ModelAdmin):
    fields = ['curriculum_id', 'curriculum_description', 'curriculum_level', 'curriculum_syllabus']
    readonly_fields = ('curriculum_id',)


admin.site.register(AcademicYear, AcademicYearsAdmin)
admin.site.register(AcademicQuarter, AcademicQuartersAdmin)
admin.site.register(Student, StudentsAdmin)
admin.site.register(Teacher, TeachersAdmin)
admin.site.register(Grade, GradesAdmin)
admin.site.register(AssignmentType, AssignmentTypesAdmin)
admin.site.register(Enrollment, EnrollmentsAdmin)
admin.site.register(Class, ClassesAdmin)
admin.site.register(Address, AddressAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Curriculum, CurriculumAdmin)
# Register your models here.
