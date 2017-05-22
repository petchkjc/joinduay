# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-04 13:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_act', models.CharField(choices=[('2', 'Activity'), ('1', 'Event')], default='2', max_length=10)),
                ('category', models.CharField(choices=[('1', 'Sport'), ('2', 'Music'), ('4', 'Club'), ('5', 'Workshop'), ('7', 'Camp'), ('8', 'Other')], default='8', max_length=20)),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=200, null=True)),
                ('speaker_name', models.CharField(blank=True, max_length=50, null=True)),
                ('date_time', models.CharField(max_length=20)),
                ('place', models.CharField(max_length=50)),
                ('college_years', models.CharField(choices=[('1', '\u0e23\u0e31\u0e1a\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e0a\u0e31\u0e49\u0e19\u0e1b\u0e35 1 \u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e48\u0e32'), ('2', '\u0e23\u0e31\u0e1a\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e0a\u0e31\u0e49\u0e19\u0e1b\u0e35 2 \u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e48\u0e32'), ('3', '\u0e23\u0e31\u0e1a\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e0a\u0e31\u0e49\u0e19\u0e1b\u0e35 3 \u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e48\u0e32'), ('4', '\u0e23\u0e31\u0e1a\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e0a\u0e31\u0e49\u0e19\u0e1b\u0e35 4 \u0e02\u0e36\u0e49\u0e19\u0e44\u0e1b\u0e2b\u0e23\u0e37\u0e2d\u0e40\u0e17\u0e35\u0e22\u0e1a\u0e40\u0e17\u0e48\u0e32'), ('5', '\u0e23\u0e31\u0e1a\u0e17\u0e38\u0e01\u0e23\u0e30\u0e14\u0e31\u0e1a\u0e0a\u0e31\u0e49\u0e19\u0e1b\u0e35')], default='5', max_length=20)),
                ('quantity', models.CharField(max_length=5)),
                ('photo', models.ImageField(upload_to='image_activity')),
                ('register_link', models.CharField(blank=True, max_length=100, null=True)),
                ('create_by_user_id', models.CharField(max_length=100)),
                ('score', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday')], default=0, null=True)),
                ('days', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('activity', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.Add_act')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.CharField(blank=True, max_length=20, null=True)),
                ('faculty', models.CharField(choices=[('1', '\u0e04\u0e13\u0e30\u0e27\u0e34\u0e17\u0e22\u0e32\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e41\u0e25\u0e30\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35'), ('2', '\u0e04\u0e13\u0e30\u0e27\u0e34\u0e28\u0e27\u0e01\u0e23\u0e23\u0e21\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('3', '\u0e04\u0e13\u0e30\u0e2a\u0e16\u0e32\u0e1b\u0e31\u0e15\u0e22\u0e01\u0e23\u0e23\u0e21\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e1c\u0e31\u0e07\u0e40\u0e21\u0e37\u0e2d\u0e07'), ('4', '\u0e04\u0e13\u0e30\u0e41\u0e1e\u0e17\u0e22\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('5', '\u0e04\u0e13\u0e30\u0e2a\u0e32\u0e18\u0e32\u0e23\u0e13\u0e2a\u0e38\u0e02\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('6', '\u0e04\u0e13\u0e30\u0e17\u0e31\u0e19\u0e15\u0e41\u0e1e\u0e17\u0e22\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('7', '\u0e04\u0e13\u0e30\u0e2a\u0e2b\u0e40\u0e27\u0e0a\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('8', '\u0e04\u0e13\u0e30\u0e1e\u0e22\u0e32\u0e1a\u0e32\u0e25\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('9', '\u0e04\u0e13\u0e30\u0e2a\u0e31\u0e07\u0e04\u0e21\u0e27\u0e34\u0e17\u0e22\u0e32\u0e41\u0e25\u0e30\u0e21\u0e32\u0e19\u0e38\u0e29\u0e22\u0e27\u0e34\u0e17\u0e22\u0e32'), ('10', '\u0e04\u0e13\u0e30\u0e28\u0e34\u0e25\u0e1b\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('11', '\u0e04\u0e13\u0e30\u0e19\u0e34\u0e15\u0e34\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('12', '\u0e04\u0e13\u0e30\u0e23\u0e31\u0e10\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('13', '\u0e04\u0e13\u0e30\u0e2a\u0e31\u0e07\u0e04\u0e21\u0e2a\u0e07\u0e40\u0e04\u0e23\u0e32\u0e30\u0e2b\u0e4c\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('14', '\u0e04\u0e13\u0e30\u0e1e\u0e32\u0e13\u0e34\u0e0a\u0e22\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e41\u0e25\u0e30\u0e01\u0e32\u0e23\u0e1a\u0e31\u0e0d\u0e0a\u0e35'), ('15', '\u0e04\u0e13\u0e30\u0e40\u0e28\u0e23\u0e29\u0e10\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('16', '\u0e04\u0e13\u0e30\u0e27\u0e32\u0e23\u0e2a\u0e32\u0e23\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e41\u0e25\u0e30\u0e2a\u0e37\u0e48\u0e2d\u0e2a\u0e32\u0e23\u0e21\u0e27\u0e25\u0e0a\u0e19'), ('17', '\u0e04\u0e13\u0e30\u0e28\u0e34\u0e25\u0e1b\u0e01\u0e23\u0e23\u0e21\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('18', '\u0e2a\u0e16\u0e32\u0e1a\u0e31\u0e19\u0e40\u0e17\u0e04\u0e42\u0e19\u0e42\u0e25\u0e22\u0e35\u0e19\u0e32\u0e19\u0e32\u0e0a\u0e32\u0e15\u0e34\u0e2a\u0e34\u0e23\u0e34\u0e19\u0e18\u0e23'), ('19', '\u0e27\u0e34\u0e17\u0e22\u0e32\u0e25\u0e31\u0e22\u0e42\u0e25\u0e01\u0e04\u0e14\u0e35\u0e28\u0e36\u0e01\u0e29\u0e32'), ('20', '\u0e27\u0e34\u0e17\u0e22\u0e32\u0e25\u0e31\u0e22\u0e41\u0e1e\u0e17\u0e22\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c\u0e19\u0e32\u0e19\u0e32\u0e0a\u0e32\u0e15\u0e34\u0e08\u0e38\u0e2c\u0e32\u0e20\u0e23\u0e13\u0e4c'), ('21', '\u0e27\u0e34\u0e17\u0e22\u0e32\u0e25\u0e31\u0e22\u0e19\u0e27\u0e31\u0e15\u0e01\u0e23\u0e23\u0e21'), ('22', '\u0e27\u0e34\u0e17\u0e22\u0e32\u0e25\u0e31\u0e22\u0e19\u0e27\u0e31\u0e15\u0e01\u0e23\u0e23\u0e21\u0e2d\u0e38\u0e14\u0e21\u0e28\u0e36\u0e01\u0e29\u0e32'), ('23', '\u0e27\u0e34\u0e17\u0e22\u0e32\u0e25\u0e31\u0e22\u0e2a\u0e2b\u0e27\u0e34\u0e17\u0e22\u0e32\u0e01\u0e32\u0e23'), ('24', '\u0e27\u0e34\u0e17\u0e22\u0e32\u0e25\u0e31\u0e22\u0e19\u0e32\u0e19\u0e32\u0e0a\u0e32\u0e15\u0e34\u0e1b\u0e23\u0e35\u0e14\u0e35 \u0e1e\u0e19\u0e21\u0e22\u0e07\u0e04\u0e4c'), ('25', '\u0e04\u0e13\u0e30\u0e40\u0e20\u0e2a\u0e31\u0e0a\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c'), ('26', '\u0e04\u0e13\u0e30\u0e27\u0e34\u0e17\u0e22\u0e32\u0e01\u0e32\u0e23\u0e40\u0e23\u0e35\u0e22\u0e19\u0e23\u0e39\u0e49\u0e41\u0e25\u0e30\u0e28\u0e36\u0e01\u0e29\u0e32\u0e28\u0e32\u0e2a\u0e15\u0e23\u0e4c')], max_length=50)),
                ('gender', models.CharField(blank=True, choices=[('1', 'Male'), ('2', 'Female')], max_length=6, null=True)),
                ('student_id', models.CharField(max_length=20)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='image_profile')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
