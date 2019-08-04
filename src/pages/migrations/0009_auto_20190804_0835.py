# Generated by Django 2.2.4 on 2019-08-04 08:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20190804_0833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='select_co',
            name='qn_num',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='total_marks',
            name='marks_for_each_qn',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='total_marks',
            name='qn_num',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)]),
        ),
    ]
