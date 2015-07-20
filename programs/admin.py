from django.contrib import admin

from programs.models import *

# class UniversityInlineAdmin(admin.TabularInline):
# 	model = University.courses.through

# class UniversityAdmin(admin.ModelAdmin):
# 	fields = ['description','departments']
# 	inlines = (UniversityInlineAdmin,)

admin.site.register(University)
admin.site.register(Program)
admin.site.register(Department)
