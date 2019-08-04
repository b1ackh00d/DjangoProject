import csv, io
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import HttpResponse
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
