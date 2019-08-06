import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.


def home_view(request, *args, **kwargs):
    return render(request, "index.html", {})

def login_view(request, *args, **kwargs):
    return render(request, "login.html", {})

def register_view(request, *args, **kwargs):
    return render(request, "register.html", {})

def upload_view(request, *args, **kwargs):
    return render(request, "upload.html", {})

def add_marks_attributes(request, cls, model, html_file):
    if request.method =="POST":
        form = cls(request.POST)
        if form.is_valid():
            form.save()
            return redirect(model)
    else:
        form =  cls()
        return render(request, html_file, {'form' : form})


def edit_attributes(request, pk, model, cls, page):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(page)
    else:
        form = cls(instance=item)
        return render(request, 'edit_attributes.html', {'form' : form})

def del_attributes(request, pk, model, html_file):
    model.objects.filter(id=pk).delete()

    items = model.objects.all()
    context = {
        'items' : items
    }
    return render(request, html_file, context)

def show_marks_attributes(request, model, html_file):
    target_stu_items = TargetCOStudent.objects.all()
    target_cls_iems = TargetCOClass.objects.all()
    items = model.objects.all()
    context = {
        'marks_items' : items,
        'target_co_stu' : target_stu_items,
        'target_co_cls' : target_cls_iems,
    }
    return render(request, html_file, context)

def add_assignment(request):
    return add_marks_attributes(request, AssignmentForm, show_assignment, 'add_assignment.html')

def add_targetCOStudentmarks(request):
    return add_marks_attributes(request, TargetCOStudentForm, show_targetCOStudentmarks, 'add_targetCOStudentmarks.html')

def add_targetCOClassmarks(request):
    return add_marks_attributes(request, TargetCOClassForm, show_targetCOClassmarks, 'add_targetCOClassmarks.html')

def add_marks_internal_one(request):
    return add_marks_attributes(request, InternalOneMarksForm, show_marks_internal_one, 'add_marks_internal_one.html')

def add_marks_internal_two(request):
    return add_marks_attributes(request, InternalTwoMarksForm, show_marks_internal_two, 'add_marks_internal_two.html')

def add_marks_semester(request):
    return add_marks_attributes(request, SemesterMarksForm, show_marks_semester, 'add_marks_semester.html')

def show_assignment(request):
    return show_marks_attributes(request, Assignment, "assignment_marks.html")

def show_targetCOStudentmarks(request):
    return show_marks_attributes(request, TargetCOStudent, "targetCOmarks.html")

def show_targetCOClassmarks(request):
    return show_marks_attributes(request, TargetCOClass, "targetCOmarks.html")

def show_marks_internal_one(request):
    return show_marks_attributes(request, Internal_one_Total_marks, "internal_one_marks.html")

def show_marks_internal_two(request):
    return show_marks_attributes(request, Internal_two_Total_marks, "internal_two_marks.html")

def show_marks_semester(request):
    return show_marks_attributes(request, Semester_Total_marks, "semester_marks.html")

def del_marks_internal_one(request, pk):
    return del_attributes(request, pk, Internal_one_Total_marks, "internal_one_marks.html")

def del_marks_internal_two(request, pk):
    return del_attributes(request, pk, Internal_two_Total_marks, "internal_two_marks.html")

def del_marks_semester(request, pk):
    return del_attributes(request, pk, Semester_Total_marks, "semester_marks.html")

def del_marks_assignment(request, pk):
    return del_attributes(request, pk, Assignment, "assignment_marks.html")

def del_marks_targetCOStudentmarks(request, pk):
    return del_attributes(request, pk, TargetCOStudent, "targetCOmarks.html")

def del_marks_targetCOClassmarks(request, pk):
    return del_attributes(request, pk, TargetCOClass, "targetCOmarks.html")

def edit_marks_internal_one(request, pk):
    return edit_attributes(request, pk, Internal_one_Total_marks, InternalOneMarksForm, "show_marks_internal_one")

def edit_marks_internal_two(request, pk):
    return edit_attributes(request, pk, Internal_two_Total_marks, InternalTwoMarksForm, "show_marks_internal_two")

def edit_marks_semester(request, pk):
    return edit_attributes(request, pk, Semester_Total_marks, SemesterMarksForm, "show_marks_semester")

def edit_marks_assignment(request, pk):
    return edit_attributes(request, pk, Assignment, AssignmentForm, "show_assignment")

def edit_marks_targetCOStudent(request, pk):
    return edit_attributes(request, pk, TargetCOStudent, TargetCOStudentForm, "show_marks_targetCOStudent")

def edit_marks_targetCOClass(request, pk):
    return edit_attributes(request, pk, TargetCOClass, TargetCOClassForm, "show_marks_targetCOClass")

def select_sub(request,*args, **kwargs):
    return render(request, "subject.html", {})

def upload_student_details(request, *args, **kwargs):
    template = "upload_student_details.html"
    prompt = {
        'order' : 'Order of csv should be id(empty), reg_num, student_name'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Student_details.objects.update_or_create(
            id = column[0],
            reg_num = column[1],
            student_name = column[2],
        )
    context = {}
    return render(request, template, context)


def upload_internal_marks(request, model,html_file):
    template = html_file
    prompt = {
        'order' : 'Order of csv should be id(empty), reg_num, student_name'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = model.objects.update_or_create(
            id = column[0],
            reg_num = column[1],
            student_name = column[2],
            qn1 = column[3],qn2 = column[4],qn3 = column[5],qn4 = column[6],qn5 = column[7],qn6 = column[8],qn7 = column[9],qn8 = column[10],qn9= column[11],qn10 = column[12],qn11= column[13],qn12 = column[14],qn13 = column[15],qn14 = column[16],qn15 = column[17],qn16 = column[18],qn17 = column[19],qn18 = column[20],qn19 = column[21]
        )
    context = {}
    return render(request, template, context)

def upload_internal_one(request):
    return upload_internal_marks(request, UploadInternalOneMarks, "upload_internal_one.html")

def upload_internal_two(request):
    return upload_internal_marks(request, UploadInternalTwoMarks, "upload_internal_two.html")

def upload_assignment_marks(request):
    template = "upload_assignment_marks.html"
    prompt = {
        'order' : 'Order of csv should be id(empty), reg_num, student_name'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = UploadAssignmentMarks.objects.update_or_create(
            id = column[0],
            reg_num = column[1],
            student_name = column[2],
            CO1 = column[3],CO2 = column[4],CO3 = column[5],CO4 = column[6],CO5 = column[7],CO6 = column[8],
        )
    context = {}
    return render(request, template, context)

def upload_semester_marks(request):
    template = "upload_semester_marks.html"
    prompt = {
        'order' : 'Order of csv should be id(empty), reg_num, student_name'
    }
    if request.method == "GET":
        return render(request, template, prompt)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'This is not a csv file')
    data_set = csv_file.read().decode('UTF-8')
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = UploadSemesterMarks.objects.update_or_create(
            id = column[0],
            reg_num = column[1],
            student_name = column[2],
            sem_marks = column[3],no_of_CO = column[4], marks_for_each_CO = column[5]
        )
    context = {}
    return render(request, template, context)

def show_students(request, *args, **kwargs):
    items = Student_details.objects.all()
    context = {
        'items' : items,
    }
    return render(request, "display_student.html", context)

def drop_table(request, model, html_file):
    model.objects.all().delete()
    return render(request, html_file, {})

def drop_student_table(request):
    return drop_table(request, Student_details, "display_student.html")

def drop_internal_one_table(request):
    return drop_table(request, UploadInternalOneMarks, "upload_internal_one.html")

def drop_internal_two_table(request):
    return drop_table(request, UploadInternalTwoMarks, "upload_internal_two.html")

def drop_assignment_table(request):
    return drop_table(request, UploadAssignmentMarks, "upload_assignment_marks.html")

def drop_semester_table(request):
    return drop_table(request, UploadSemesterMarks, "upload_semester_marks.html")
