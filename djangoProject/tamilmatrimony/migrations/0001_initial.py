# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-02 02:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tamilmatrimony.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='profiles',
            fields=[
                ('tmId', models.AutoField(primary_key=True, serialize=False)),
                ('pId', models.CharField(default=b'TMG', max_length=10)),
                ('slug', models.SlugField(unique=True)),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, default=b'/media/default/pimage.png', null=True, upload_to=tamilmatrimony.models.upload_location)),
                ('maritalStatus', models.CharField(choices=[(b'single', b'Single'), (b'married', b'Married'), (b'divorced', b'Divorced')], default=b'single', max_length=25)),
                ('body_Type', models.CharField(max_length=15)),
                ('height', models.CharField(max_length=15)),
                ('weight', models.CharField(max_length=15)),
                ('matrimonyProfileFor', models.CharField(choices=[(b'son', b'Son'), (b'daughter', b'Daughter'), (b'brother', b'Brother'), (b'sister', b'Sister'), (b'self', b'Self')], default=b'personal', max_length=25)),
                ('drink', models.CharField(max_length=15)),
                ('smoke', models.CharField(max_length=15)),
                ('dateOfBirth', models.DateTimeField(verbose_name=b'Date of Birth/Time - Format : YYYY-MM-DD HH:MM')),
                ('updated', models.DateTimeField(auto_now=True)),
                ('age', models.IntegerField(default=0)),
                ('motherTongue', models.CharField(max_length=50)),
                ('gender', models.CharField(choices=[(b'male', b'Male'), (b'female', b'Female')], max_length=15)),
                ('blood_group', models.CharField(default=b'not specified', max_length=20)),
                ('diet', models.CharField(max_length=20)),
                ('religion', models.CharField(choices=[(b'hindu', b'Hindu'), (b'cristian', b'Cristian'), (b'muslim', b'Muslim'), (b'sikh', b'Sikh'), (b'buddhist', b'Buddhist')], max_length=50)),
                ('caste', models.CharField(max_length=50)),
                ('sub_caste', models.CharField(max_length=25)),
                ('placeOfBirth', models.CharField(max_length=30)),
                ('rassi', models.CharField(max_length=30)),
                ('education', models.CharField(max_length=50)),
                ('education_detail', models.CharField(max_length=50)),
                ('occupation_detail', models.CharField(max_length=100)),
                ('annual_income', models.CharField(default=b'not specified', max_length=20)),
                ('current_location', models.CharField(max_length=25)),
                ('father_occupation', models.CharField(max_length=50)),
                ('mother_occupation', models.CharField(max_length=50)),
                ('no_of_sisters', models.IntegerField(default=0)),
                ('no_of_brother', models.IntegerField(default=0)),
                ('p_age_min', models.IntegerField(default=0)),
                ('p_age_max', models.IntegerField(default=0)),
                ('p_Marital_Status', models.CharField(max_length=10)),
                ('p_Body_Type', models.CharField(max_length=25)),
                ('p_Complexion', models.CharField(max_length=25)),
                ('p_Height', models.CharField(max_length=25)),
                ('p_Diet', models.CharField(max_length=25)),
                ('p_Manglik', models.CharField(max_length=25)),
                ('p_Religion', models.CharField(max_length=25)),
                ('p_Caste', models.CharField(max_length=25)),
                ('p_Mother_Tongue', models.CharField(max_length=25)),
                ('p_Education', models.CharField(max_length=25)),
                ('p_Country_Of_Residence', models.CharField(max_length=25)),
                ('p_State', models.CharField(max_length=25)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]