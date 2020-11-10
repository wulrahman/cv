# Generated by Django 3.1.3 on 2020-11-09 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=200)),
                ('comapny_name', models.CharField(max_length=200)),
                ('job_start', models.DateTimeField(verbose_name='Job Start')),
                ('job_end', models.DateTimeField(verbose_name='Job End')),
            ],
        ),
    ]
