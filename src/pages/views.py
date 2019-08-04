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
    items = model.objects.all()
    context = {
        'marks_items' : items,
    }
    return render(request, html_file, context)

def add_assignment(request):
    return add_marks_attributes(request, AssignmentForm, show_assignment, 'add_assignment.html')

def add_marks_internal_one(request):
    return add_marks_attributes(request, InternalOneMarksForm, show_marks_internal_one, 'add_marks_internal_one.html')

def add_marks_internal_two(request):
    return add_marks_attributes(request, InternalTwoMarksForm, show_marks_internal_two, 'add_marks_internal_two.html')

def add_marks_semester(request):
    return add_marks_attributes(request, SemesterMarksForm, show_marks_semester, 'add_marks_semester.html')

def show_assignment(request):
    return show_marks_attributes(request, Assignment, "assignment_marks.html")

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

def edit_marks_internal_one(request, pk):
    return edit_attributes(request, pk, Internal_one_Total_marks, InternalOneMarksForm, "show_marks_internal_one")

def edit_marks_internal_two(request, pk):
    return edit_attributes(request, pk, Internal_two_Total_marks, InternalTwoMarksForm, "show_marks_internal_two")

def edit_marks_semester(request, pk):
    return edit_attributes(request, pk, Semester_Total_marks, SemesterMarksForm, "show_marks_semester")

def edit_marks_assignment(request, pk):
    return edit_attributes(request, pk, Assignment, AssignmentForm, "show_assignment")


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

def show_students(request, *args, **kwargs):
    items = Student_details.objects.all()
    context = {
        'items' : items,
    }
    return render(request, "display_student.html", context)

def drop_table(request, *args, **kwargs):
    Student_details.objects.all().delete()
    return render(request, "display_student.html", {})
