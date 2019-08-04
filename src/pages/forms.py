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
        fields = ('qn_num', 'marks_for_each_qn', 'CO_for_each_qn')

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('co_num', 'total_marks_for_co')

class TargetCOForm(forms.ModelForm):
    class Meta:
        model = TargetCO
        fields = ('co_num', 'target_co')
