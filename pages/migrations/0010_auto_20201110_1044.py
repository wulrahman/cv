# Generated by Django 3.1.3 on 2020-11-10 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_education_course_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='course_type',
            field=models.CharField(choices=[("Bachelor's degree", "Bachelor's degree"), ("Master's degree", "Master's degree"), ('AS Level', 'AS Level'), ('GCSE', 'GCSE')], default='GCSE', max_length=20),
        ),
    ]
