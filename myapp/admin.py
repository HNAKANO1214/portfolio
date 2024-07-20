from django.conf import settings
from django.contrib import admin
from myapp.forms import (
    ProfileForm, WorkForm, ExperienceForm, EducationForm, SoftwareForm, TechnicalForm
)
from myapp.models import Education, Experience, Profile, Work, Software, Technical


admin.site.site_header = f'{settings.SITE_TITLE} 管理サイト'
admin.site.index_title = 'モデル管理'


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileForm
    list_display = ('id', 'title', 'name')


class WorkAdmin(admin.ModelAdmin):
    form = WorkForm
    list_display = ('id', 'title')


class ExperienceAdmin(admin.ModelAdmin):
    form = ExperienceForm
    list_display = ('id', 'occupation', 'company', 'period')


class EducationAdmin(admin.ModelAdmin):
    form = EducationForm
    list_display = ('id', 'course', 'school', 'period')


class SoftwareAdmin(admin.ModelAdmin):
    form = SoftwareForm
    list_display = ('id', 'name', 'level', 'percentage')


class TechnicalAdmin(admin.ModelAdmin):
    form = TechnicalForm
    list_display = ('id', 'name', 'level', 'percentage')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Technical, TechnicalAdmin)
