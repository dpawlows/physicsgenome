from django.contrib import admin

from programs.models import *

class ProgramInline(admin.TabularInline):
	model = Program
	extra = 3

class DepartmentAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields':['description','universities']}),
	]

	inlines = [ProgramInline]

class DepartmentInline(admin.TabularInline):
	model = Department
	extra = 0
	fields = ('description',)

class UniversityAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields':['description'],
		'classes':('extrapretty',)
		}),
	]
	

	inlines = [DepartmentInline]

admin.site.register(University,UniversityAdmin)
admin.site.register(Program)
admin.site.register(Department,DepartmentAdmin)

