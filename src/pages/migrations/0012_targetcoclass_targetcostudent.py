# Generated by Django 2.2.4 on 2019-08-06 18:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20190805_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='TargetCOClass',
            fields=[
                ('targetco_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.TargetCO')),
            ],
            bases=('pages.targetco',),
        ),
        migrations.CreateModel(
            name='TargetCOStudent',
            fields=[
                ('targetco_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pages.TargetCO')),
            ],
            bases=('pages.targetco',),
        ),
    ]
