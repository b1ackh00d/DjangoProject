import csv, io, itertools
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import permission_required
from django.db.models import *
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
        'range' : range(1, Student_details.objects.count() + 1),
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


def upload_internal_one(request):
    template = "upload_internal_one.html"
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
        _, created = UploadInternalOneMarks.objects.update_or_create(
            id = column[0],
            reg_num = column[1],
            student_name = column[2],
            qn1 = column[3],qn2 = column[4],qn3 = column[5],qn4 = column[6],qn5 = column[7],qn6 = column[8],qn7 = column[9],qn8 = column[10],qn9= column[11],qn10 = column[12],qn11= column[13],qn12 = column[14],qn13 = column[15],qn14 = column[16],qn15 = column[17],qn16 = column[18],qn17 = column[19],qn18 = column[20],qn19 = column[21]
        )
    context = {}
    return render(request, template, context)

def upload_internal_two(request):
    template = "upload_internal_two.html"
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
        _, created = UploadInternalTwoMarks.objects.update_or_create(
            id = column[0],
            reg_num = column[1],
            student_name = column[2],
            qn1 = column[3],qn2 = column[4],qn3 = column[5],qn4 = column[6],qn5 = column[7],qn6 = column[8],qn7 = column[9],qn8 = column[10],qn9= column[11],qn10 = column[12],qn11= column[13],qn12 = column[14],qn13 = column[15],qn14 = column[16],qn15 = column[17],qn16 = column[18],qn17 = column[19],qn18 = column[20],qn19 = column[21]
        )
    context = {}
    return render(request, template, context)

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
            grade = column[3]
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



# Calculations

#returns assignment_total_marks_of a single student for any CO
def func1(id__1, cls, co):
     cos = ['CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6']
     co_in = "CO" + str(co)
     if co_in in cos:
         t = list(cls.objects.filter(id = id__1).values())
         return float(t[0].get(co_in))
     else:
         return float(0)

#returns semester mark of a single student
def func2(id__1, cls):
    if (Semester_Total_marks.objects.all().values()[0].get('regulation') == 17):
        regulation = {'A': 75.5, 'A+': 85.5, 'B': 55, 'B+': 65.5, 'O': 95.5, 'RA': 24.5, 'RA-AB': 0, 'SA': 0, 'W': 0} #R2017
    elif (Semester_Total_marks.objects.all().values()[0].get('regulation') == 15):
        regulation = {'A': 74.5, 'A+': 84.5, 'B': 54.5, 'B+': 64.5, 'O': 95, 'RA': 24.5, 'RA-AB': 0, 'U': 0, 'W': 0} #R2015
    else:
        return float(0)
    l = list(cls.objects.filter(id = id__1).values())
    if l[0].get('grade') in regulation:
        return float(regulation[l[0].get('grade')])

#returns total marks of a student for a given CO
def func(id__1, cls, co, c_o):
    l = list(Semester_Total_marks.objects.all().values())
    total_co =  l[0].get('no_of_CO')
    if (c_o <= total_co):
        total = 0
        l = list(cls.objects.filter(id = id__1).values())
        for i in co:
             for j in l[0]:
                     if (i == j):
                             total += l[0].get(j)
        assignment_marks = func1(id__1, UploadAssignmentMarks, c_o)
        semester_marks = func2(id__1, UploadSemesterMarks) / total_co
        return float(total) + assignment_marks + semester_marks
    else:
        return 0
     # func(i => studend_id, UploadInternalTwoMarks, giveCOqns(Internal_two_Total_marks, 3)

def giveCOqns(cls, co):
     res = []
     for i in cls.objects.filter(CO_for_each_qn=co):
             res.append("qn" + str(i.qn_num))
     return res

def return_totalmarks(i, internalone, internaltwo, assignment, semester):
    l = list(Semester_Total_marks.objects.all().values())
    if (i <= l[0].get('no_of_CO')):
        total_internal_one = internalone.objects.filter(CO_for_each_qn=i).aggregate(Sum('marks_for_each_qn'))['marks_for_each_qn__sum']
        total_internal_two = internaltwo.objects.filter(CO_for_each_qn=i).aggregate(Sum('marks_for_each_qn'))['marks_for_each_qn__sum']
        if (total_internal_one is None):
            total_internal_one = 0
        if (total_internal_two is None):
            total_internal_two = 0
        total_assignment = assignment.objects.filter(co_num=i).aggregate(Sum('total_marks_for_co'))['total_marks_for_co__sum']
        sem_total = list(semester.objects.all().values())
        total_semester = 100 /l[0].get('no_of_CO')
        return float(total_internal_one) + float(total_internal_two) + total_assignment + total_semester
    else:
        return 1
# for i in range(1, Student_details.objects.count() + 1):
#     t = func(i, UploadInternalOneMarks, giveCOqns(Internal_one_Total_marks, 1),1) / return_totalmarks(1, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
#     print(round(t, 3))

def total():
    TotalCOStudent.objects.all().delete()
    for i in range(1, Student_details.objects.count() + 1):
        c1 = func(i, UploadInternalOneMarks, giveCOqns(Internal_one_Total_marks, 1),1) / return_totalmarks(1, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
        c2 = func(i, UploadInternalOneMarks, giveCOqns(Internal_one_Total_marks, 2),2) / return_totalmarks(2, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
        c3 = func(i, UploadInternalTwoMarks, giveCOqns(Internal_two_Total_marks, 3),3) / return_totalmarks(3, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
        c4 = func(i, UploadInternalTwoMarks, giveCOqns(Internal_two_Total_marks, 4),4) / return_totalmarks(4, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
        c5 = func(i, UploadInternalTwoMarks, giveCOqns(Internal_two_Total_marks, 5),5) / return_totalmarks(5, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
        c6 = func(i, UploadInternalTwoMarks, giveCOqns(Internal_two_Total_marks, 6),6) / return_totalmarks(6, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks) * 100
        l = Student_details.objects.filter(id = i).values()
        total = TotalCOStudent(reg_num = l[0].get('reg_num'), student_name = l[0].get('student_name'), co1 = c1, co2 = c2, co3 = c3, co4 = c4, co5 = c5, co6 = c6)
        total.save()

def calculate_CO(request, *args, **kwargs):
    total()
    return render(request, "subject.html", {'form' : 'Calculated, Press Dispaly Button'})

def show_CO_result(request):
    return show_marks_attributes(request, TotalCOStudent, "total_co_student.html")

def result_detail(request):
    l = list(Semester_Total_marks.objects.all().values())
    no_of_CO = l[0].get('no_of_CO')
    weightage_of_CO = {}
    above_target = {}
    final_achievement = {}
    above_target_class = above_Targetclass()
    achieved_or_not = {}
    target_co_student = TargetCOStudent.objects.all()
    target_student = {}
    for i in range(1, no_of_CO + 1):
        weightage_of_CO.update({ i : str(return_totalmarks(i, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks))})
        above_target.update({ i : str(students_above_targetMarks(i))})
        target_student.update({ i : float(target_co_student.filter(id = i).values()[0].get('target_co')) })
        t = (float(above_target[i]) / Student_details.objects.count()) * 100
        final_achievement.update({i : round(t, 2)})
        if (final_achievement[i] >= above_target_class.get(i)):
            achieved_or_not.update({ i : 'Achieved'})
        else:
            achieved_or_not.update({ i : 'Not Achieved'})
    context = {
        'achieve_or_not' : achieved_or_not,
        'total' : Student_details.objects.count(),
        'no_of_CO' : no_of_CO,
        'target_co_student' : target_student,
        'weightage' : weightage_of_CO,
        'above_target' : above_target,
        'final_achievement' : final_achievement
    }
    return render(request, "result_detail.html", context)

def students_above_targetMarks(co):
    l = list(Semester_Total_marks.objects.all().values())
    no_of_CO = l[0].get('no_of_CO')
    count = 0
    if(co <= no_of_CO):
        for i in range(1, Student_details.objects.count() + 1):
            l =list(TargetCOStudent.objects.filter(co_num = co).values())
            target = float(l[0].get('target_co'))
            p = list(Student_details.objects.filter(id = i).values())[0].get('reg_num')
            k = list(TotalCOStudent.objects.filter(reg_num = p).values())[0].get('co' + str(co))
            if(k >= target):
                count+=1
        return count
    else:
        return 0

def above_Targetclass():
     achieve_or_not = {}
     # l = list(Semester_Total_marks.objects.all().values())
     for i in range(1, 7):
         t = TargetCOClass.objects.filter(co_num = i).values()
         achieve_or_not.update( { i : float(t[0].get('target_co'))} )
     return achieve_or_not

# download-csv_file

def download_result(request):

    items = TotalCOStudent.objects.all()
    count = Student_details.objects.count()

    l = list(Semester_Total_marks.objects.all().values())
    no_of_CO = l[0].get('no_of_CO')
    weightage_of_CO = {}
    above_target = {}
    target_student = {}
    final_achievement = {}
    above_target_class = above_Targetclass()
    achieved_or_not = {}
    target_co_student = TargetCOStudent.objects.all()
    for i in range(1, 7):
        if (i > no_of_CO):
            weightage_of_CO.update({ i : '-'})
        else:
            weightage_of_CO.update({ i : str(return_totalmarks(i, Internal_one_Total_marks, Internal_two_Total_marks, Assignment, Semester_Total_marks))})
        above_target.update({ i : str(students_above_targetMarks(i))})
        t = (float(above_target[i]) / Student_details.objects.count()) * 100
        final_achievement.update({i : round(t, 2)})
        target_student.update({i : float(list(target_co_student.filter(co_num = i).values())[0].get('target_co'))})
        if (final_achievement[i] >= above_target_class.get(i)):
            if (i > no_of_CO):
                achieved_or_not.update({ i : '-'})
            else:
                achieved_or_not.update({ i : 'Achieved'})
        else:
            if (i > no_of_CO):
                achieved_or_not.update({ i : '-'})
            else:
                achieved_or_not.update({ i : 'Not Achieved'})

    response = HttpResponse(content_type="text/csv")
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response, delimiter = ',')
    writer.writerow(['Id', 'Reg_Num', 'Student_Name', 'CO1', 'CO2', 'CO3', 'CO4', 'CO5', 'CO6'])
    weightageCO = [' ', ' ', ' Total Weightage of COs -->',weightage_of_CO[1],weightage_of_CO[2],weightage_of_CO[3],weightage_of_CO[4],weightage_of_CO[5],weightage_of_CO[6] ]
    writer.writerow(weightageCO)
    for (i, obj) in zip(range(1, count + 1), items):
        writer.writerow([i, obj.reg_num, obj.student_name, obj.co1, obj.co2, obj.co3, obj.co4, obj.co5, obj.co6])
    writer.writerow([' ',' ',' ',' ',' ',' ',' ',' ',' '])
    target_marks = [' ', ' ', ' Target Marks',target_student[1],target_student[2],target_student[3],target_student[4],target_student[5],target_student[6] ]
    writer.writerow(target_marks)
    above_target_marks = [' ', ' ', ' No.of students who have secured above Target Marks',above_target[1],above_target[2],above_target[3],above_target[4],above_target[5],above_target[6] ]
    writer.writerow(above_target_marks)
    final_achievement = [' ', ' ', '% of students achieved CO',final_achievement[1],final_achievement[2],final_achievement[3],final_achievement[4],final_achievement[5],final_achievement[6] ]
    writer.writerow(final_achievement)
    achieved_or_not = [' ', ' ', 'Overall CO Result',achieved_or_not[1],achieved_or_not[2],achieved_or_not[3],achieved_or_not[4],achieved_or_not[5],achieved_or_not[6] ]
    writer.writerow(achieved_or_not)


    return response

# pattern
def qn_pattern(request, cls, html_file):
    cls.objects.all().delete()
    if (cls == Internal_two_Total_marks):
        for i in range(1, 20):
            if (i >= 11 and i<=15):
                t = cls(qn_num = i, marks_for_each_qn = 2, CO_for_each_qn = 3)
            elif (i>=16 and i<=19):
                t = cls(qn_num = i, marks_for_each_qn = 10, CO_for_each_qn = 3)
            else:
                t = cls(qn_num = i, marks_for_each_qn = 1, CO_for_each_qn = 3)
            t.save()
    else:
        for i in range(1, 20):
            if (i >= 11 and i<=15):
                t = cls(qn_num = i, marks_for_each_qn = 2, CO_for_each_qn = 1)
            elif (i>=16 and i<=19):
                t = cls(qn_num = i, marks_for_each_qn = 10, CO_for_each_qn = 1)
            else:
                t = cls(qn_num = i, marks_for_each_qn = 1, CO_for_each_qn = 1)
            t.save()
    return render(request, html_file, {})

def pattern_one_internal_one(request):
    qn_pattern(request, Internal_one_Total_marks, "internal_one_marks.html")
    return show_marks_attributes(request, Internal_one_Total_marks, "internal_one_marks.html")

def pattern_one_internal_two(request):
    qn_pattern(request, Internal_two_Total_marks, "internal_two_marks.html")
    return show_marks_attributes(request, Internal_two_Total_marks, "internal_two_marks.html")

# pattern two , pattern three and so on
