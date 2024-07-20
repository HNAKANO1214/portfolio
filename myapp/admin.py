from django.conf import settings
from django.contrib import admin
from image_cropping import ImageCroppingMixin

from myapp.forms import ProfileForm
from myapp.models import Education, Experience, Profile, Work, Software, Technical


admin.site.site_header = f'{settings.SITE_TITLE} 管理サイト'
admin.site.index_title = 'モデル管理'


class ProfileAdmin(ImageCroppingMixin, admin.ModelAdmin):
    form = ProfileForm
    list_display = ('id', 'title', 'name')


class WorkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id', 'occupation', 'company', 'period')


class EducationAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'school', 'period')


class SoftwareAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'percentage')


class TechnicalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'level', 'percentage')


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Work, WorkAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Software, SoftwareAdmin)
admin.site.register(Technical, TechnicalAdmin)
