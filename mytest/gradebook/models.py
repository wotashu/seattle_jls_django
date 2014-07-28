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

