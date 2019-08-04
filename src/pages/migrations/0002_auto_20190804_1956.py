# Generated by Django 2.2.4 on 2019-08-04 19:56

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_num', models.IntegerField(choices=[(1, 'CO1'), (2, 'CO2'), (3, 'CO3'), (4, 'CO4'), (5, 'CO5'), (6, 'CO6')], default=1)),
                ('total_marks_for_co', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
            ],
        ),
        migrations.CreateModel(
            name='Internal_one_Total_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn_num', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('marks_for_each_qn', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('CO_for_each_qn', models.IntegerField(choices=[(1, 'CO1'), (2, 'CO2'), (3, 'CO3'), (4, 'CO4'), (5, 'CO5')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Internal_two_Total_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn_num', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('marks_for_each_qn', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('CO_for_each_qn', models.IntegerField(choices=[(1, 'CO1'), (2, 'CO2'), (3, 'CO3'), (4, 'CO4'), (5, 'CO5')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Semester_Total_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn_num', models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('marks_for_each_qn', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)])),
                ('CO_for_each_qn', models.IntegerField(choices=[(1, 'CO1'), (2, 'CO2'), (3, 'CO3'), (4, 'CO4'), (5, 'CO5')], default=1)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TargetCO',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co_num', models.IntegerField(choices=[(1, 'CO1'), (2, 'CO2'), (3, 'CO3'), (4, 'CO4'), (5, 'CO5'), (6, 'CO6')], default=1)),
                ('target_co', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='UploadAssignmentMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=50)),
                ('CO1', models.DecimalField(decimal_places=2, max_digits=50)),
                ('CO2', models.DecimalField(decimal_places=2, max_digits=50)),
                ('CO3', models.DecimalField(decimal_places=2, max_digits=50)),
                ('CO4', models.DecimalField(decimal_places=2, max_digits=50)),
                ('CO5', models.DecimalField(decimal_places=2, max_digits=50)),
                ('CO6', models.DecimalField(decimal_places=2, max_digits=50)),
            ],
        ),
        migrations.CreateModel(
            name='UploadMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reg_num', models.CharField(max_length=10)),
                ('student_name', models.CharField(max_length=50)),
                ('qn1', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn2', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn3', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn4', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn5', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn6', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn7', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn8', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn9', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn10', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn11', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn12', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn13', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn14', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn15', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn16', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn17', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn18', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
                ('qn19', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_name',
            field=models.CharField(max_length=50),
        ),
        migrations.CreateModel(
            name='UploadInternalOneMarks',
            fields=[
                ('uploadmarks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.UploadMarks')),
            ],
            bases=('pages.uploadmarks',),
        ),
        migrations.CreateModel(
            name='UploadInternalTwoMarks',
            fields=[
                ('uploadmarks_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.UploadMarks')),
            ],
            bases=('pages.uploadmarks',),
        ),
    ]
