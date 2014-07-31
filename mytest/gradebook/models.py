from django.db import models

# Create your models here.


class Academicquarters(models.Model):
    academicquarterid = models.IntegerField(db_column='AcademicQuarterID', primary_key=True) # Field name made lowercase.
    academicquartername = models.CharField(db_column='AcademicQuarterName', max_length=45, blank=True) # Field name made lowercase.
    academicquarterstartdate = models.DateField(db_column='AcademicQuarterStartDate', blank=True, null=True) # Field name made lowercase.
    academicquarterenddate = models.DateField(db_column='AcademicQuarterEndDate', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcademicQuarters'

    def __unicode__(self):
        return self.academicquartername


class Academicyears(models.Model):
    academicyearid = models.IntegerField(db_column='AcademicYearID', primary_key=True) # Field name made lowercase.
    academicyeartitle = models.CharField(db_column='AcademicYearTitle', max_length=45, blank=True) # Field name made lowercase.
    academicyearstartdate = models.DateField(db_column='AcademicYearStartDate', blank=True, null=True) # Field name made lowercase.
    academicyearenddate = models.DateField(db_column='AcademicYearEndDate', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AcademicYears'

    def __unicode__(self):
        return self.academicyeartitle


class Addresses(models.Model):
    addressid = models.IntegerField(db_column='AddressID', primary_key=True) # Field name made lowercase.
    addressstreet1 = models.CharField(db_column='AddressStreet1', max_length=45, blank=True) # Field name made lowercase.
    addressstreet2 = models.CharField(db_column='AddressStreet2', max_length=45, blank=True) # Field name made lowercase.
    addresscity = models.CharField(db_column='AddressCity', max_length=45, blank=True) # Field name made lowercase.
    addresssstate = models.CharField(db_column='AddressSstate', max_length=45, blank=True) # Field name made lowercase.
    addresszip = models.CharField(db_column='AddressZIP', max_length=45, blank=True) # Field name made lowercase.
    addresscountry = models.CharField(db_column='AddressCountry', max_length=45, blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Addresses'

    def __unicode__(self):
        return self.addressstreet1


class Emergencycontacts(models.Model):
    emergencyid = models.IntegerField(db_column='EmergencyID', primary_key=True) # Field name made lowercase.
    emergencyrelationship = models.CharField(db_column='EmergencyRelationship', max_length=45) # Field name made lowercase.
    emergencyemail = models.CharField(db_column='EmergencyEmail', max_length=45, blank=True) # Field name made lowercase.
    emergencyphone = models.CharField(db_column='EmergencyPhone', max_length=45, blank=True) # Field name made lowercase.
    addresses_addressid = models.ForeignKey(Addresses, db_column='Addresses_AddressID', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EmergencyContacts'

    def __unicode__(self):
        return self.emergencyid


class Assignmenttypes(models.Model):
    assignmenttypeid = models.IntegerField(db_column='AssignmentTypeID', primary_key=True) # Field name made lowercase.
    assignmenttitle = models.CharField(db_column='AssignmentTitle', max_length=70, blank=True) # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'AssignmentTypes'
    def __unicode__(self):
        return self.assignmenttitle


class Courses(models.Model):
    courseid = models.IntegerField(db_column='CourseID', primary_key=True) # Field name made lowercase.
    courselevel = models.CharField(db_column='CourseLevel', max_length=45, blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Courses'

    def __unicode__(self):
        return self.courselevel


class Students(models.Model):
    studentid = models.IntegerField(db_column='StudentID', primary_key=True) # Field name made lowercase.
    studentlastname = models.CharField(db_column='StudentLastName', max_length=225) # Field name made lowercase.
    studentfirstname = models.CharField(db_column='StudentFirstName', max_length=225) # Field name made lowercase.
    studentalternativename = models.CharField(db_column='StudentAlternativeName', max_length=45, blank=True) # Field name made lowercase.
    studentbirthdate = models.DateField(db_column='StudentBirthdate', blank=True, null=True) # Field name made lowercase.
    studentemail = models.CharField(db_column='StudentEmail', max_length=225, blank=True) # Field name made lowercase.
    studentphone = models.CharField(db_column='StudentPhone', max_length=225, blank=True) # Field name made lowercase.
    emergencycontact_emergencyid = models.ForeignKey(Emergencycontacts, db_column='EmergencyContact_EmergencyID', blank=True, null=True) # Field name made lowercase.
    addresses_addressid = models.ForeignKey(Addresses, db_column='Addresses_AddressID', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Students'

    def __unicode__(self):
        return u'%s, %s' % (self.studentlastname, self.studentfirstname)


class Parents(models.Model):
    parentid = models.IntegerField(db_column='ParentID', primary_key=True) # Field name made lowercase.
    parentfirstname = models.CharField(db_column='ParentFirstname', max_length=45, blank=True) # Field name made lowercase.
    parentlastname = models.CharField(db_column='ParentLastname', max_length=45, blank=True) # Field name made lowercase.
    parentrelationship = models.CharField(db_column='ParentRelationship', max_length=45, blank=True) # Field name made lowercase.
    parentemail = models.CharField(db_column='ParentEmail', max_length=45, blank=True) # Field name made lowercase.
    parentphone = models.CharField(db_column='ParentPhone', max_length=45, blank=True) # Field name made lowercase.
    address_addressid = models.ForeignKey(Addresses, db_column='Address_AddressID', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Parents'

    def __unicode__(self):
        return self.parentfirstname


class Families(models.Model):
    students_studentid = models.ForeignKey('Students', db_column='Students_StudentID') # Field name made lowercase.
    parent_parentid = models.ForeignKey('Parents', db_column='Parent_parentID') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Families'


class Teachers(models.Model):
    teacherid = models.IntegerField(db_column='TeacherID', primary_key=True) # Field name made lowercase.
    teacherlastname = models.CharField(db_column='TeacherLastName', max_length=225) # Field name made lowercase.
    teacherfirstname = models.CharField(db_column='TeacherFirstName', max_length=225, blank=True) # Field name made lowercase.
    teacheremail = models.CharField(db_column='TeacherEmail', max_length=225, blank=True) # Field name made lowercase.
    teacherphone = models.CharField(db_column='TeacherPhone', max_length=45, blank=True) # Field name made lowercase.
    address_addressid = models.IntegerField(db_column='Address_AddressID', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Teachers'

    def __unicode__(self):
        return u'%s, %s' % (self.teacherlastname, self.teacherfirstname)


class Curriculums(models.Model):
    curriculumid = models.IntegerField(db_column='CurriculumID', primary_key=True) # Field name made lowercase.
    curriculmdescription = models.CharField(db_column='CurriculmDescription', max_length=45, blank=True) # Field name made lowercase.
    curriculumlevel = models.CharField(db_column='CurriculumLevel', max_length=45, blank=True) # Field name made lowercase.
    curriculumsyllabus = models.CharField(db_column='CurriculumSyllabus', max_length=45, blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Curriculums'

    def __unicode__(self):
        return self.curriculums


class Rooms(models.Model):
    roomid = models.IntegerField(db_column='RoomID', primary_key=True) # Field name made lowercase.
    building = models.CharField(db_column='Building', max_length=225) # Field name made lowercase.
    capacity = models.CharField(db_column='Capacity', max_length=225) # Field name made lowercase.
    equipment = models.CharField(db_column='Equipment', max_length=225) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Rooms'

    def __unicode__(self):
        return self.roomid


class Schedules(models.Model):
    scheduleid = models.IntegerField(db_column='ScheduleID', primary_key=True) # Field name made lowercase.
    dayoftheweek = models.CharField(db_column='DayOfTheWeek', max_length=225) # Field name made lowercase.
    starttime = models.TimeField(db_column='StartTime') # Field name made lowercase.
    endtime = models.TimeField(db_column='EndTime') # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Schedules'

    def __unicode__(self):
        return self.scheduleid


class Classes(models.Model):
    classid = models.IntegerField(db_column='ClassID', primary_key=True) # Field name made lowercase.
    academicyears_academicyearid = models.ForeignKey(Academicyears, db_column='AcademicYears_AcademicYearID') # Field name made lowercase.
    academicquarters_academicquarterid = models.ForeignKey(Academicquarters, db_column='AcademicQuarters_AcademicQuarterID') # Field name made lowercase.
    courses_courseid = models.ForeignKey('Courses', db_column='Courses_CourseID') # Field name made lowercase.
    classsection = models.CharField(db_column='ClassSection', max_length=45, blank=True) # Field name made lowercase.
    teachers_teacherid = models.ForeignKey('Teachers', db_column='Teachers_TeacherID') # Field name made lowercase.
    rooms_roomid = models.ForeignKey('Rooms', db_column='Rooms_RoomID', blank=True, null=True) # Field name made lowercase.
    schedules_scheduleid = models.ForeignKey('Schedules', db_column='Schedules_ScheduleID', blank=True, null=True) # Field name made lowercase.
    curriculums_curriculumid = models.ForeignKey('Curriculums', db_column='Curriculums_CurriculumID', blank=True, null=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Classes'

    def __unicode__(self):
        return u'(%s %s) %s %s: %s ' % (self.academicyears_academicyearid, self.academicquarters_academicquarterid, self.courses_courseid, self.classsection, self.teachers_teacherid)


class Enrollments(models.Model):
    enrollmentid = models.IntegerField(db_column='EnrollmentID', primary_key=True) # Field name made lowercase.
    classes_classid = models.ForeignKey(Classes, db_column='Classes_ClassID') # Field name made lowercase.
    students_studentid = models.ForeignKey('Students', db_column='Students_StudentID') # Field name made lowercase.
    dropstatus = models.IntegerField(db_column='DropStatus', blank=True, null=True) # Field name made lowercase.
    attendancetotal = models.IntegerField(db_column='AttendanceTotal', blank=True, null=True) # Field name made lowercase.
    attendancescore = models.IntegerField(db_column='AttendanceScore', blank=True, null=True) # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Enrollments'

    def __unicode__(self):
        return self.enrollmentid


class Grades(models.Model):
    gradeid = models.IntegerField(db_column='GradeID', primary_key=True) # Field name made lowercase.
    enrollments_enrollmentid = models.ForeignKey(Enrollments, db_column='Enrollments_EnrollmentID') # Field name made lowercase.
    assignmenttypes_assignmenttypeid = models.ForeignKey(Assignmenttypes, db_column='AssignmentTypes_AssignmentTypeID') # Field name made lowercase.
    gradescore = models.CharField(db_column='GradeScore', max_length=45, blank=True) # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Grades'

    def __unicode__(self):
        return self.gradescore









