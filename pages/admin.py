from django.contrib import admin
from .models import Experience, Skill, Education

# Register your models here.
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'company_name')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('skill_name', 'skill_type', 'skill_level')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('course_name', 'academy_name')

admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)

admin.site.register(Skill, SkillAdmin)