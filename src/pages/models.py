from django.db import models

# Create your models here.

class Student_details(models.Model):

    reg_num = models.CharField(max_length=10, blank=False)
    student_name = models.CharField(max_length=50, blank=False)

    def __str__(self):
        return 'Reg Num : {0} Name : {1}'.format(self.reg_num, self.student_name)
