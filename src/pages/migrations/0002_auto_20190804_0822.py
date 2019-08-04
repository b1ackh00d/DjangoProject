# Generated by Django 2.2.4 on 2019-08-04 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Select_Co',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn_num', models.IntegerField()),
                ('CO_for_each_qn', models.IntegerField(choices=[('CO1', 'Course Outcome 1'), ('CO2', 'Course Outcome 2'), ('CO3', 'Course Outcome 3'), ('CO4', 'Course Outcome 4'), ('CO5', 'Course Outcome 5')])),
            ],
        ),
        migrations.CreateModel(
            name='Total_marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qn_num', models.IntegerField()),
                ('marks_for_each_qn', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='student_details',
            name='student_name',
            field=models.CharField(max_length=50),
        ),
    ]
