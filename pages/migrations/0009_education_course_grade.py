# Generated by Django 3.1.3 on 2020-11-10 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='course_grade',
            field=models.CharField(default='', max_length=200),
        ),
    ]