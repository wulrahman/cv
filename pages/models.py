from django.db import models
from os.path import splitext, basename
import uuid

# Create your models here.
def image_upload_to(instance, filename):
    base, ext = splitext(filename)
    newname = "%s%s" % (uuid.uuid4(), ext)
    return "static/image/{}".format(newname)

class Experience(models.Model):
    job_title = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    job_start = models.DateTimeField('Job Start')
    job_end = models.DateTimeField('Job End')
    # company_logo = models.URLField(max_length=200)
    image = models.ImageField(default="", upload_to=image_upload_to)


class Skill(models.Model):
    skill_name = models.CharField(max_length=200)
    SKILL_LEVEL = [
        ('AV', 'Advanced'),
        ('IM', 'Intermediate'),
        ('B', 'Beginner')
    ]
    SKILL_TYPE = [
        ('E', 'Endorsements'),
        ('IK', 'Industry Knowledge'),
        ('TT', 'Tools & Technologies'),
        ('IS', 'Interpersonal Skills'),
        ('L', 'Languages'),
        ('OS', 'Other Skills')
    ]
    skill_type = models.CharField(
        max_length=2,
        choices=SKILL_TYPE,
        default='OS',
    )
    skill_level = models.CharField(
        max_length=2,
        choices=SKILL_LEVEL,
        default='B',
    )

class Education(models.Model):
    academy_name = models.CharField(max_length=200)
    course_name = models.CharField(max_length=200)
    course_grade = models.CharField(max_length=200, default="")
    course_start = models.DateTimeField('Job Start')
    course_end = models.DateTimeField('Job End')
    # academy_logo = models.URLField(max_length=200)
    image = models.ImageField(default="", upload_to=image_upload_to)

    COURSE_TYPE = [
        ('Bachelor\'s degree', 'Bachelor\'s degree'),
        ('Master\'s degree', 'Master\'s degree'),
        ('AS Level', 'AS Level'),
        ('GCSE', 'GCSE')
    ]
    course_type = models.CharField(
        max_length=20,
        choices=COURSE_TYPE,
        default='GCSE',
    )