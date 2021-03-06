from django.db import models

# Create your models here.


class AcademicQuarter(models.Model):
    academic_quarter_id = models.IntegerField(db_column='AcademicQuarterID',
                                              primary_key=True)  # Field name made lowercase.
    academic_quarter_name = models.CharField(db_column='AcademicQuarterName', max_length=45,
                                             blank=True)  # Field name made lowercase.
    academic_quarter_start_date = models.DateField(db_column='AcademicQuarterStartDate', blank=True,
                                                   null=True)  # Field name made lowercase.
    academic_quarter_end_date = models.DateField(db_column='AcademicQuarterEndDate', blank=True,
                                                 null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcademicQuarters'

    def __unicode__(self):
        return unicode(self.academic_quarter_name)


class AcademicYear(models.Model):
    academic_year_id = models.AutoField(db_column='AcademicYearID', primary_key=True)
    academic_year_title = models.CharField(db_column='AcademicYearTitle', max_length=45,
                                           blank=True)
    academic_year_start_date = models.DateField(db_column='AcademicYearStartDate', blank=True,
                                                null=True)
    academic_year_end_date = models.DateField(db_column='AcademicYearEndDate', blank=True,
                                              null=True)

    class Meta:
        managed = False
        db_table = 'AcademicYears'
        ordering = ('-academic_year_title',)

    def __unicode__(self):
        return unicode(self.academic_year_title)


class Address(models.Model):
    address_id = models.AutoField(db_column='AddressID', primary_key=True)
    address_street_1 = models.CharField(db_column='AddressStreet1', max_length=45,
                                        blank=True)  # Field name made lowercase.
    address_street_2 = models.CharField(db_column='AddressStreet2', max_length=45,
                                        blank=True)  # Field name made lowercase.
    address_city = models.CharField(db_column='AddressCity', max_length=45, blank=True)  # Field name made lowercase.
    address_state = models.CharField(db_column='AddressState', max_length=45,
                                     blank=True)  # Field name made lowercase.
    address_zip = models.CharField(db_column='AddressZIP', max_length=45, blank=True)  # Field name made lowercase.
    address_country = models.CharField(db_column='AddressCountry', max_length=45,
                                       blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Addresses'
        verbose_name_plural = "addresses"
        ordering = ('address_street_1', 'address_street_2',)

    def __unicode__(self):
        # return unicode(self.address_id)
        return u'%s, %s, %s, %s, %s' % (self.address_street_1, self.address_street_2, self.address_city,
                                        self.address_state, self.address_zip)


class EmergencyContact(models.Model):
    emergency_id = models.AutoField(db_column='EmergencyID', primary_key=True)  # Field name made lowercase.
    emergency_relationship = models.CharField(db_column='EmergencyRelationship',
                                              max_length=45)  # Field name made lowercase.
    emergency_email = models.CharField(db_column='EmergencyEmail', max_length=45,
                                       blank=True)  # Field name made lowercase.
    emergency_phone = models.CharField(db_column='EmergencyPhone', max_length=45,
                                       blank=True)  # Field name made lowercase.
    addresses_address_id = models.ForeignKey(Address, db_column='Addresses_AddressID', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmergencyContacts'

    def __unicode__(self):
        return unicode(self.emergency_id)


class AssignmentType(models.Model):
    assignment_type_id = models.AutoField(db_column='AssignmentTypeID', primary_key=True)
    assignment_title = models.CharField(db_column='AssignmentTitle', max_length=70,
                                        blank=True)

    class Meta:
        managed = False
        db_table = 'AssignmentTypes'

    def __unicode__(self):
        return unicode(self.assignment_title)


class Course(models.Model):
    course_id = models.AutoField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    course_level = models.CharField(db_column='CourseLevel', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Courses'

    def __unicode__(self):
        return unicode(self.course_level)


class Student(models.Model):
    student_id = models.AutoField(db_column='StudentID', primary_key=True)  # Field name made lowercase.
    student_last_name = models.CharField(db_column='StudentLastName', max_length=225)  # Field name made lowercase.
    student_first_name = models.CharField(db_column='StudentFirstName', max_length=225)  # Field name made lowercase.
    student_alternative_name = models.CharField(db_column='StudentAlternativeName', max_length=45,
                                                blank=True)  # Field name made lowercase.
    student_birth_date = models.DateField(db_column='StudentBirthDate', blank=True,
                                          null=True)  # Field name made lowercase.
    student_email = models.CharField(db_column='StudentEmail', max_length=225, blank=True)  # Field name made lowercase.
    student_phone = models.CharField(db_column='StudentPhone', max_length=225, blank=True)  # Field name made lowercase.
    emergency_contact_emergency_id = models.ForeignKey(EmergencyContact, db_column='EmergencyContact_EmergencyID',
                                                       blank=True, null=True)  # Field name made lowercase.
    addresses_address_id = models.ForeignKey(Address, db_column='Addresses_AddressID', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Students'
        ordering = ('student_last_name', 'student_first_name')

    def __unicode__(self):
        # return unicode(self.student_id) or u'%s, %s' % (self.student_last_name, self.student_first_name)
        return u'%s, %s' % (self.student_last_name, self.student_first_name)


class Parent(models.Model):
    parent_id = models.AutoField(db_column='ParentID', primary_key=True)  # Field name made lowercase.
    parent_first_name = models.CharField(db_column='ParentFirstName', max_length=45,
                                         blank=True)  # Field name made lowercase.
    parent_last_name = models.CharField(db_column='ParentLastName', max_length=45,
                                        blank=True)  # Field name made lowercase.
    parent_relationship = models.CharField(db_column='ParentRelationship', max_length=45,
                                           blank=True)  # Field name made lowercase.
    parent_email = models.CharField(db_column='ParentEmail', max_length=45, blank=True)  # Field name made lowercase.
    parent_phone = models.CharField(db_column='ParentPhone', max_length=45, blank=True)  # Field name made lowercase.
    address_address_id = models.ForeignKey(Address, db_column='Address_AddressID', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parents'
        ordering = ('parent_last_name', 'parent_first_name',)

    def __unicode__(self):
        return unicode(self.parent_id) or u'%s, %s' % (self.parent_last_name, self.parent_first_name)
        # return u'%s, %s' % (self.parent_last_name, self.parent_first_name)


class Family(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    students_student_id = models.ForeignKey(Student, db_column='Students_StudentID')  # Field name made lowercase.
    parent_parent_id = models.ForeignKey(Parent, db_column='Parent_parentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Families'
        verbose_name_plural = "families"


class Teacher(models.Model):
    teacher_id = models.AutoField(db_column='TeacherID', primary_key=True)  # Field name made lowercase.
    teacher_last_name = models.CharField(db_column='TeacherLastName', max_length=225)  # Field name made lowercase.
    teacher_first_name = models.CharField(db_column='TeacherFirstName', max_length=225,
                                          blank=True)  # Field name made lowercase.
    teacher_email = models.CharField(db_column='TeacherEmail', max_length=225, blank=True)  # Field name made lowercase.
    teacher_phone = models.CharField(db_column='TeacherPhone', max_length=45, blank=True)  # Field name made lowercase.
    address_address_id = models.IntegerField(db_column='Address_AddressID', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teachers'
        ordering = ('teacher_last_name', 'teacher_first_name',)

    def __unicode__(self):
        #return unicode(self.teacher_id) or
        return u'%s, %s' % (self.teacher_last_name, self.teacher_first_name)


class Curriculum(models.Model):
    curriculum_id = models.AutoField(db_column='CurriculumID', primary_key=True)  # Field name made lowercase.
    curriculum_description = models.CharField(db_column='CurriculumDescription', max_length=45,
                                              blank=True)  # Field name made lowercase.
    curriculum_level = models.CharField(db_column='CurriculumLevel', max_length=45,
                                        blank=True)  # Field name made lowercase.
    curriculum_syllabus = models.CharField(db_column='CurriculumSyllabus', max_length=45,
                                           blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curriculums'

    def __unicode__(self):
        return unicode(self.curriculum_id)


class Room(models.Model):
    room_id = models.AutoField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=225, blank=True)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=225, blank=True)  # Field name made lowercase.
    equipment = models.CharField(db_column='Equipment', max_length=225, blank=True)  # Field name made lowercase.
    room_number = models.CharField(max_length=225, blank=True)

    class Meta:
        # managed = True
        db_table = 'Rooms'

    def __unicode__(self):
        return unicode(self.room_id)


class Schedule(models.Model):
    schedule_id = models.AutoField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    day_of_the_week = models.CharField(db_column='DayOfTheWeek', max_length=225)  # Field name made lowercase.
    start_time = models.TimeField(db_column='StartTime')  # Field name made lowercase.
    end_time = models.TimeField(db_column='EndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedules'

    def __unicode__(self):
        return unicode(self.schedule_id)


class Class(models.Model):
    class_id = models.AutoField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    academic_years_academic_year_id = models.ForeignKey(AcademicYear,
                                                        db_column='AcademicYears_AcademicYearID')
    academic_quarters_academic_quarter_id = models.ForeignKey(AcademicQuarter,
                                                              db_column='AcademicQuarters_AcademicQuarterID')
    courses_course_id = models.ForeignKey(Course, db_column='Courses_CourseID')  # Field name made lowercase.
    class_section = models.CharField(db_column='ClassSection', max_length=45, blank=True)  # Field name made lowercase.
    teachers_teacher_id = models.ForeignKey(Teacher, db_column='Teachers_TeacherID')  # Field name made lowercase.
    rooms_room_id = models.ForeignKey(Room, db_column='Rooms_RoomID', blank=True,
                                      null=True)  # Field name made lowercase.
    schedules_schedule_id = models.ForeignKey(Schedule, db_column='Schedules_ScheduleID', blank=True,
                                              null=True)  # Field name made lowercase.
    curriculums_curriculum_id = models.ForeignKey(Curriculum, db_column='Curriculums_CurriculumID', blank=True,
                                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'
        verbose_name_plural = "classes"
        ordering = ('academic_years_academic_year_id', 'academic_quarters_academic_quarter_id', 'courses_course_id',
                    'class_section', 'teachers_teacher_id',)

    def __unicode__(self):
        return u'(%s %s) %s %s: %s ' % (
            self.academic_years_academic_year_id, self.academic_quarters_academic_quarter_id, self.courses_course_id,
            self.class_section, self.teachers_teacher_id)


class Enrollment(models.Model):
    enrollment_id = models.AutoField(db_column='EnrollmentID', primary_key=True)  # Field name made lowercase.
    classes_class_id = models.ForeignKey(Class, db_column='Classes_ClassID')  # Field name made lowercase.
    students_student_id = models.ForeignKey(Student, db_column='Students_StudentID')  # Field name made lowercase.
    drop_status = models.IntegerField(db_column='DropStatus', blank=True, null=True)  # Field name made lowercase.
    attendance_total = models.IntegerField(db_column='AttendanceTotal', blank=True,
                                           null=True)  # Field name made lowercase.
    attendance_score = models.IntegerField(db_column='AttendanceScore', blank=True,
                                           null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enrollments'

    def __unicode__(self):
        return unicode(self.enrollment_id)

    def edit_grades(self):
        if self.enrollment_id:
            return "<a href='/admin/gradebook/enrollment/%s' target='_blank'>Edit</a>" % str(self.enrollment_id)
        else:
            return "Not present"

    def student_name(self):
        return "%s, %s" % (self.students_student_id.student_last_name,
                           self.students_student_id.student_first_name)

    student_name.short_description = 'student name'

    def class_information(self):
        return "(%s %s) %s %s: %s, %s" % (
            self.classes_class_id.academic_years_academic_year_id,
            self.classes_class_id.academic_quarters_academic_quarter_id,
            self.classes_class_id.courses_course_id,
            self.classes_class_id.class_section,
            self.classes_class_id.teachers_teacher_id.teacher_last_name,
            self.classes_class_id.teachers_teacher_id.teacher_first_name
        )

    class_information.short_description = 'class information'

    edit_grades.allow_tags = True


class Grade(models.Model):
    grade_id = models.AutoField(db_column='GradeID', primary_key=True)  # Field name made lowercase.
    enrollments_enrollment_id = models.ForeignKey(Enrollment,
                                                  db_column='Enrollments_EnrollmentID')  # Field name made lowercase.
    assignment_types_assignment_type_id = models.ForeignKey(AssignmentType,
                                                            db_column='AssignmentTypes_AssignmentTypeID')
    grade_score = models.CharField(db_column='GradeScore', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grades'

    def __unicode__(self):
        return unicode(self.grade_score)
