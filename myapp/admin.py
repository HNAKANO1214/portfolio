from django.contrib import admin
from .models import Education, Experience, Profile, Work, Software, Technical

admin.site.register(Profile)
admin.site.register(Work)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Software)
admin.site.register(Technical)
