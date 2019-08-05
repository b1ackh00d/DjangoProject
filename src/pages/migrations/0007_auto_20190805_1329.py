# Generated by Django 2.2.4 on 2019-08-05 13:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20190805_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='total_marks_for_co',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='uploadassignmentmarks',
            name='CO1',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
        migrations.AlterField(
            model_name='uploadassignmentmarks',
            name='CO2',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
        migrations.AlterField(
            model_name='uploadassignmentmarks',
            name='CO3',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
        migrations.AlterField(
            model_name='uploadassignmentmarks',
            name='CO4',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
        migrations.AlterField(
            model_name='uploadassignmentmarks',
            name='CO5',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
        migrations.AlterField(
            model_name='uploadassignmentmarks',
            name='CO6',
            field=models.DecimalField(decimal_places=4, max_digits=5),
        ),
    ]
