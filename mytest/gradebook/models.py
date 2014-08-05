from django.db import models

# Create your models here.


class AcademicQuarters(models.Model):
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
        return self.academic_quarter_name


class AcademicYears(models.Model):
    academic_year_id = models.IntegerField(db_column='AcademicYearID', primary_key=True)
    academic_year_title = models.CharField(db_column='AcademicYearTitle', max_length=45,
                                           blank=True)
    academic_year_start_date = models.DateField(db_column='AcademicYearStartDate', blank=True,
                                                null=True)
    academic_year_end_date = models.DateField(db_column='AcademicYearEndDate', blank=True,
                                              null=True)

    class Meta:
        managed = False
        db_table = 'AcademicYears'

    def __unicode__(self):
        return self.academic_year_title


class Addresses(models.Model):
    address_id = models.IntegerField(db_column='AddressID', primary_key=True)
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

    def __unicode__(self):
        return self.address_id


class EmergencyContacts(models.Model):
    emergency_id = models.IntegerField(db_column='EmergencyID', primary_key=True)  # Field name made lowercase.
    emergency_relationship = models.CharField(db_column='EmergencyRelationship',
                                              max_length=45)  # Field name made lowercase.
    emergency_email = models.CharField(db_column='EmergencyEmail', max_length=45,
                                       blank=True)  # Field name made lowercase.
    emergency_phone = models.CharField(db_column='EmergencyPhone', max_length=45,
                                       blank=True)  # Field name made lowercase.
    addresses_address_id = models.ForeignKey(Addresses, db_column='Addresses_AddressID', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmergencyContacts'

    def __unicode__(self):
        return self.emergencyid


class AssignmentTypes(models.Model):
    assignment_type_id = models.IntegerField(db_column='AssignmentTypeID', primary_key=True)
    assignment_title = models.CharField(db_column='AssignmentTitle', max_length=70,
                                        blank=True)

    class Meta:
        managed = False
        db_table = 'AssignmentTypes'

    def __unicode__(self):
        return self.assignment_title


class Courses(models.Model):
    course_id = models.IntegerField(db_column='CourseID', primary_key=True)  # Field name made lowercase.
    course_level = models.CharField(db_column='CourseLevel', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Courses'

    def __unicode__(self):
        return self.course_level


class Students(models.Model):
    student_id = models.IntegerField(db_column='StudentID', primary_key=True)  # Field name made lowercase.
    student_last_name = models.CharField(db_column='StudentLastName', max_length=225)  # Field name made lowercase.
    student_first_name = models.CharField(db_column='StudentFirstName', max_length=225)  # Field name made lowercase.
    student_alternative_name = models.CharField(db_column='StudentAlternativeName', max_length=45,
                                                blank=True)  # Field name made lowercase.
    student_birth_date = models.DateField(db_column='StudentBirthDate', blank=True,
                                          null=True)  # Field name made lowercase.
    student_email = models.CharField(db_column='StudentEmail', max_length=225, blank=True)  # Field name made lowercase.
    student_phone = models.CharField(db_column='StudentPhone', max_length=225, blank=True)  # Field name made lowercase.
    emergency_contact_emergency_id = models.ForeignKey(EmergencyContacts, db_column='EmergencyContact_EmergencyID',
                                                       blank=True, null=True)  # Field name made lowercase.
    addresses_address_id = models.ForeignKey(Addresses, db_column='Addresses_AddressID', blank=True,
                                             null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Students'

    def __unicode__(self):
        #return self.student_id
        return u'%s, %s' % (self.student_last_name, self.student_first_name)


class Parents(models.Model):
    parent_id = models.IntegerField(db_column='ParentID', primary_key=True)  # Field name made lowercase.
    parent_first_name = models.CharField(db_column='ParentFirstName', max_length=45,
                                         blank=True)  # Field name made lowercase.
    parent_last_name = models.CharField(db_column='ParentLastName', max_length=45,
                                        blank=True)  # Field name made lowercase.
    parent_relationship = models.CharField(db_column='ParentRelationship', max_length=45,
                                           blank=True)  # Field name made lowercase.
    parent_email = models.CharField(db_column='ParentEmail', max_length=45, blank=True)  # Field name made lowercase.
    parent_phone = models.CharField(db_column='ParentPhone', max_length=45, blank=True)  # Field name made lowercase.
    address_address_id = models.ForeignKey(Addresses, db_column='Address_AddressID', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parents'

    def __unicode__(self):
        return u'%s, %s' % (self.parent_last_name, self.parent_first_name)


class Families(models.Model):
    students_student_id = models.ForeignKey('Students', db_column='Students_StudentID')  # Field name made lowercase.
    parent_parent_id = models.ForeignKey('Parents', db_column='Parent_parentID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Families'


class Teachers(models.Model):
    teacher_id = models.IntegerField(db_column='TeacherID', primary_key=True)  # Field name made lowercase.
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

    def __unicode__(self):
        return u'%s, %s' % (self.teacher_last_name, self.teacher_first_name)


class Curriculums(models.Model):
    curriculum_id = models.IntegerField(db_column='CurriculumID', primary_key=True)  # Field name made lowercase.
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
        return self.curriculum_id


class Rooms(models.Model):
    room_id = models.IntegerField(db_column='RoomID', primary_key=True)  # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=225)  # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=225)  # Field name made lowercase.
    equipment = models.CharField(db_column='Equipment', max_length=225)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rooms'

    def __unicode__(self):
        return self.room_id


class Schedules(models.Model):
    schedule_id = models.IntegerField(db_column='ScheduleID', primary_key=True)  # Field name made lowercase.
    day_of_the_week = models.CharField(db_column='DayOfTheWeek', max_length=225)  # Field name made lowercase.
    start_time = models.TimeField(db_column='StartTime')  # Field name made lowercase.
    end_time = models.TimeField(db_column='EndTime')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedules'

    def __unicode__(self):
        return self.schedule_id


class Classes(models.Model):
    class_id = models.IntegerField(db_column='ClassID', primary_key=True)  # Field name made lowercase.
    academic_years_academic_year_id = models.ForeignKey(AcademicYears,
                                                        db_column='AcademicYears_AcademicYearID')
    academic_quarters_academic_quarter_id = models.ForeignKey(AcademicQuarters,
                                                              db_column='AcademicQuarters_AcademicQuarterID')
    courses_course_id = models.ForeignKey('Courses', db_column='Courses_CourseID')  # Field name made lowercase.
    class_section = models.CharField(db_column='ClassSection', max_length=45, blank=True)  # Field name made lowercase.
    teachers_teacher_id = models.ForeignKey('Teachers', db_column='Teachers_TeacherID')  # Field name made lowercase.
    rooms_room_id = models.ForeignKey('Rooms', db_column='Rooms_RoomID', blank=True,
                                      null=True)  # Field name made lowercase.
    schedules_schedule_id = models.ForeignKey('Schedules', db_column='Schedules_ScheduleID', blank=True,
                                              null=True)  # Field name made lowercase.
    curriculums_curriculum_id = models.ForeignKey('Curriculums', db_column='Curriculums_CurriculumID', blank=True,
                                                  null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'

    def __unicode__(self):
        return u'(%s %s) %s %s: %s ' % (
            self.academic_years_academic_year_id, self.academic_quarters_academic_quarter_id, self.courses_course_id,
            self.class_section, self.teachers_teacher_id)


class Enrollments(models.Model):
    enrollment_id = models.IntegerField(db_column='EnrollmentID', primary_key=True)  # Field name made lowercase.
    classes_class_id = models.ForeignKey(Classes, db_column='Classes_ClassID')  # Field name made lowercase.
    students_student_id = models.ForeignKey('Students', db_column='Students_StudentID')  # Field name made lowercase.
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
        return unicode(self.enrollment_id) or u''


class Grades(models.Model):
    grade_id = models.IntegerField(db_column='GradeID', primary_key=True)  # Field name made lowercase.
    enrollments_enrollment_id = models.ForeignKey(Enrollments,
                                                  db_column='Enrollments_EnrollmentID')  # Field name made lowercase.
    assignment_types_assignment_type_id = models.ForeignKey(AssignmentTypes,
                                                            db_column='AssignmentTypes_AssignmentTypeID')
    grade_score = models.CharField(db_column='GradeScore', max_length=45, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grades'

    def __unicode__(self):
        return self.grade_score









