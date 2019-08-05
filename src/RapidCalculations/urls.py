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
    path('upload_internal_one/', upload_internal_one, name="upload_internal_one"),
    path('upload_internal_two/', upload_internal_two, name="upload_internal_two"),
    path('upload_assignment_marks/', upload_assignment_marks, name="upload_assignment_marks"),
    path('upload_semester_marks/', upload_semester_marks, name="upload_semester_marks"),
    path('Subject/', select_sub, name="select_sub"),
    path('show_marks_internal_one/', show_marks_internal_one, name="show_marks_internal_one"),
    path('show_marks_internal_two/', show_marks_internal_two, name="show_marks_internal_two"),
    path('show_marks_semester/', show_marks_semester, name="show_marks_semester"),
    path('show_marks_targetCO/', show_targetCOmarks, name="show_marks_targetCO"),
    path('add_marks_internal_one/', add_marks_internal_one, name="add_marks_internal_one"),
    path('add_marks_internal_two/', add_marks_internal_two, name="add_marks_internal_two"),
    path('add_marks_semester/', add_marks_semester, name="add_marks_semester"),
    path('add_marks_targetCO/', add_targetCOmarks, name="add_marks_targetCO"),
    path('edit_marks_internal_one/<pk>/', edit_marks_internal_one, name='edit_marks_internal_one'),
    path('edit_marks_internal_two/<pk>/', edit_marks_internal_two, name='edit_marks_internal_two'),
    path('edit_marks_semester/<pk>/', edit_marks_semester, name='edit_marks_semester'),
    path('edit_marks_targetCO/<pk>/', edit_marks_targetCO, name='edit_marks_targetCO'),
    path('delete_marks_internal_one/<pk>/', del_marks_internal_one, name='del_marks_internal_one'),
    path('delete_marks_internal_two/<pk>/', del_marks_internal_two, name='del_marks_internal_two'),
    path('delete_marks_semester/<pk>/', del_marks_semester, name='del_marks_semester'),
    path('delete_marks_targetCO/<pk>/', del_marks_targetCOmarks, name='del_marks_targetCOmarks'),
    path('show_assignment/', show_assignment, name='show_assignment'),
    path('add_assignment/', add_assignment, name='add_assignment'),
    path('delete_marks_assignment/<pk>/', del_marks_assignment, name='del_marks_assignment'),
    path('edit_marks_assignment/<pk>/', edit_marks_assignment, name='edit_marks_assignment'),
    path('delete/', drop_student_table, name="drop_student_table"),
    path('delete_internal_one_table/', drop_internal_one_table, name="drop_internal_one_table"),
    path('delete_internal_two_table/', drop_internal_two_table, name="drop_internal_two_table"),
    path('delete_assignment_table/', drop_assignment_table, name="drop_assignment_table"),
    path('delete_semester_table/', drop_semester_table, name="drop_semester_table"),
    path('admin/', admin.site.urls, name="admin"),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
