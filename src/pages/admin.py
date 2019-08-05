from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportModelAdmin
@admin.register(Student_details)
@admin.register(Internal_one_Total_marks)
@admin.register(Internal_two_Total_marks)
@admin.register(Semester_Total_marks)
@admin.register(Assignment)
@admin.register(TargetCO)
@admin.register(UploadInternalOneMarks)
@admin.register(UploadInternalTwoMarks)
@admin.register(UploadAssignmentMarks)
@admin.register(UploadSemesterMarks)

class ViewStudentDetails(ImportExportModelAdmin):
    pass
