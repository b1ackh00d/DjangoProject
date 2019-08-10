"""RapidCalculations URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from pages.views import *

urlpatterns = [
    path('', home_view, name="home"),
    path('login/', login_view, name="login"),
    path('register/', register_view, name="register"),
    path('upload/', upload_view, name="upload"),
    path('display_student/', show_students, name="display_student"),
    path('upload_student/', upload_student_details, name="upload_student"),
    path('Subject/upload_internal_one/', upload_internal_one, name="upload_internal_one"),
    path('Subject/upload_internal_two/', upload_internal_two, name="upload_internal_two"),
    path('Subject/upload_assignment_marks/', upload_assignment_marks, name="upload_assignment_marks"),
    path('Subject/upload_semester_marks/', upload_semester_marks, name="upload_semester_marks"),
    path('Subject/', select_sub, name="select_sub"),
    path('Result/', show_CO_result, name = "show_CO_result"),
    path('Result/detailed_result', result_detail, name = "result_detail"),
    path('Calculate_CO/', calculate_CO, name = "calculate_CO"),
    path('Subject/show_marks_internal_one/', show_marks_internal_one, name="show_marks_internal_one"),
    path('Subject/show_marks_internal_two/', show_marks_internal_two, name="show_marks_internal_two"),
    path('Subject/show_marks_semester/', show_marks_semester, name="show_marks_semester"),
    path('Subject/show_marks_targetCOStudent/', show_targetCOStudentmarks, name="show_marks_targetCOStudent"),
    path('Subject/show_marks_targetCOClass/', show_targetCOClassmarks, name="show_marks_targetCOClass"),
    path('Subject/add_marks_internal_one/', add_marks_internal_one, name="add_marks_internal_one"),
    path('Subject/add_marks_internal_two/', add_marks_internal_two, name="add_marks_internal_two"),
    path('Subject/add_marks_semester/', add_marks_semester, name="add_marks_semester"),
    path('Subject/add_marks_targetCOStudent/', add_targetCOStudentmarks, name="add_marks_targetCOStudent"),
    path('Subject/add_marks_targetCOClass/', add_targetCOClassmarks, name="add_marks_targetCOClass"),
    path('Subject/edit_marks_internal_one/<pk>/', edit_marks_internal_one, name='edit_marks_internal_one'),
    path('Subject/edit_marks_internal_two/<pk>/', edit_marks_internal_two, name='edit_marks_internal_two'),
    path('Subject/edit_marks_semester/<pk>/', edit_marks_semester, name='edit_marks_semester'),
    path('Subject/edit_marks_targetCOStudent/<pk>/', edit_marks_targetCOStudent, name='edit_marks_targetCOStudent'),
    path('Subject/edit_marks_targetCOClass/<pk>/', edit_marks_targetCOClass, name='edit_marks_targetCOClass'),
    path('Subject/delete_marks_internal_one/<pk>/', del_marks_internal_one, name='del_marks_internal_one'),
    path('Subject/delete_marks_internal_two/<pk>/', del_marks_internal_two, name='del_marks_internal_two'),
    path('Subject/delete_marks_semester/<pk>/', del_marks_semester, name='del_marks_semester'),
    path('Subject/delete_marks_targetCOStudent/<pk>/', del_marks_targetCOStudentmarks, name='del_marks_targetCOStudentmarks'),
    path('Subject/delete_marks_targetCOClass/<pk>/', del_marks_targetCOClassmarks, name='del_marks_targetCOClassmarks'),
    path('Subject/show_assignment/', show_assignment, name='show_assignment'),
    path('Subject/add_assignment/', add_assignment, name='add_assignment'),
    path('Subject/delete_marks_assignment/<pk>/', del_marks_assignment, name='del_marks_assignment'),
    path('Subject/edit_marks_assignment/<pk>/', edit_marks_assignment, name='edit_marks_assignment'),
    path('Subject/delete/', drop_student_table, name="drop_student_table"),
    path('Subject/delete_internal_one_table/', drop_internal_one_table, name="drop_internal_one_table"),
    path('Subject/delete_internal_two_table/', drop_internal_two_table, name="drop_internal_two_table"),
    path('Subject/delete_assignment_table/', drop_assignment_table, name="drop_assignment_table"),
    path('Subject/delete_semester_table/', drop_semester_table, name="drop_semester_table"),
    path('admin/', admin.site.urls, name="admin"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
