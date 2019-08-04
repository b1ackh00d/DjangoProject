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
        (5, 'CO5')
    )
    co_num = models.IntegerField(choices=choices, default = 1)
    total_marks_for_co = models.IntegerField(blank=False,
    validators=[MaxValueValidator(10), MinValueValidator(1)])

    def __str__(self):
        return 'CO type : {0} CO_weightage : {1}'.format(self.co_num, self.total_marks_for_co)

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
