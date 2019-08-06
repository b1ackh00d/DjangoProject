from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Student_details(models.Model):

    reg_num = models.CharField(max_length=10, blank=False)
    student_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return 'Reg Num : {0} Name : {1}'.format(self.reg_num, self.student_name)

class Assignment(models.Model):
    choices = (
        (1, 'CO1'),
        (2, 'CO2'),
        (3, 'CO3'),
        (4, 'CO4'),
        (5, 'CO5'),
        (6, 'CO6')
    )
    co_num = models.IntegerField(choices=choices, default = 1)
    total_marks_for_co = models.IntegerField(blank=False,
    validators=[MaxValueValidator(10), MinValueValidator(0)])

    def __str__(self):
        return 'CO type : {0} CO_weightage : {1}'.format(self.co_num, self.total_marks_for_co)

class TargetCO(models.Model):
    choices = (
        (1, 'CO1'),
        (2, 'CO2'),
        (3, 'CO3'),
        (4, 'CO4'),
        (5, 'CO5'),
        (6, 'CO6')
    )
    co_num = models.IntegerField(choices=choices, default = 1)
    target_co = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return 'CO type : {0} Target CO mark : {1}'.format(self.co_num, self.target_co)

class TargetCOStudent(TargetCO):
    pass

class TargetCOClass(TargetCO):
    pass

class Total_marks(models.Model):
    qn_num = models.IntegerField(blank=False,
    validators=[MaxValueValidator(20), MinValueValidator(1)])
    marks_for_each_qn = models.IntegerField(blank=False,
    validators=[MaxValueValidator(10), MinValueValidator(1)])
    choices = (
        (1, 'CO1'),
        (2, 'CO2'),
        (3, 'CO3'),
        (4, 'CO4'),
        (5, 'CO5')
    )
    CO_for_each_qn = models.IntegerField(choices=choices, default = 1)

    class Meta:
        abstract = True

    def __str__(self):
        return 'Qn num : {0} Marks : {1} CO_type : {2}'.format(self.qn_num, self.marks_for_each_qn, self.CO_for_each_qn)

class Internal_one_Total_marks(Total_marks):
    pass

class Internal_two_Total_marks(Total_marks):
    pass

class Semester_Total_marks(Total_marks):
    pass

class UploadAssignmentMarks(models.Model):

    reg_num = models.CharField(max_length=10, blank=False)
    student_name = models.CharField(max_length=50, blank=False)
    CO1 = models.DecimalField(max_digits=6, decimal_places=4)
    CO2 = models.DecimalField(max_digits=6, decimal_places=4)
    CO3 = models.DecimalField(max_digits=6, decimal_places=4)
    CO4 = models.DecimalField(max_digits=6, decimal_places=4)
    CO5 = models.DecimalField(max_digits=6, decimal_places=4)
    CO6 = models.DecimalField(max_digits=6, decimal_places=4)

class UploadSemesterMarks(models.Model):
    reg_num = models.CharField(max_length=10, blank=False)
    student_name = models.CharField(max_length=50, blank=False)
    sem_marks = models.DecimalField(max_digits=7, decimal_places=4)
    no_of_CO = models.IntegerField(default=1,validators=[MaxValueValidator(10), MinValueValidator(1)])
    marks_for_each_CO = models.IntegerField(blank=False,validators=[MaxValueValidator(50), MinValueValidator(1)])

class UploadMarks(models.Model):
    # id = models.AutoField(primary_key=True)
    reg_num = models.CharField(max_length=10, blank=False)
    student_name = models.CharField(max_length=50, blank=False)

    qn1 = models.IntegerField(default=0,validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn2 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn3 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn4 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn5 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn6 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn7 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn8 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn9 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn10 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn11 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn12 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn13 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn14 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn15 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn16 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn17 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn18 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    qn19 = models.IntegerField(default=0,
    validators=[MaxValueValidator(20), MinValueValidator(0)])

    def __str__(self):
        return 'Reg Num : {0} Name : {1}'.format(self.reg_num, self.student_name)

class UploadInternalOneMarks(UploadMarks):
    pass


class UploadInternalTwoMarks(UploadMarks):
    pass
