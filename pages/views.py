from django.shortcuts import render
from django.http import HttpResponse
from .models import Experience, Skill, Education

# Create your views here.
def homePageView(request):
    experience_all = Experience.objects.all
    E = Skill.objects.filter(skill_type__exact="E")
    IK = Skill.objects.filter(skill_type__exact="IK")
    TT = Skill.objects.filter(skill_type__exact="TT")
    IS = Skill.objects.filter(skill_type__exact="IS")
    L = Skill.objects.filter(skill_type__exact="L")
    OS = Skill.objects.filter(skill_type__exact="OS")

    education_all = Education.objects.all

    return render(request, "pages/index.html", context={
        'experience': experience_all, 
        'education':education_all,
        'E':E,
        'IK':IK,
        'TT':TT,
        'IS':IS,
        'L':L,
        'OS':OS
        })