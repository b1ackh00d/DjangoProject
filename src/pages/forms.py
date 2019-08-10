from django import forms
from .models import *

class InternalOneMarksForm(forms.ModelForm):
    class Meta:
        model = Internal_one_Total_marks
        fields = ('qn_num', 'marks_for_each_qn', 'CO_for_each_qn')

class InternalTwoMarksForm(forms.ModelForm):
    class Meta:
        model = Internal_two_Total_marks
        fields = ('qn_num', 'marks_for_each_qn', 'CO_for_each_qn')

class SemesterMarksForm(forms.ModelForm):
    class Meta:
        model = Semester_Total_marks
        fields = ('regulation', 'no_of_CO')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('co_num', 'total_marks_for_co')

class TargetCOStudentForm(forms.ModelForm):
    class Meta:
        model = TargetCOStudent
        fields = ('co_num', 'target_co')

class TargetCOClassForm(forms.ModelForm):
    class Meta:
        model = TargetCOClass
        fields = ('co_num', 'target_co')

class TotalCOStudentForm(forms.ModelForm):
    class Meta:
        model = TotalCOStudent
        fields = ('co1', 'co2', 'co3', 'co4', 'co4', 'co5', 'co6')
