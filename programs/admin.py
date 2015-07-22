from django.contrib import admin
from django import forms
from programs.models import *

class ProgramInline(admin.TabularInline):
	model = Program
	extra = 3

class DepartmentAdmin(admin.ModelAdmin):

	fieldsets = [
	(None, {'fields':['description','universities']}),
	]
	list_display = ('description','universities',)
	inlines = [ProgramInline]

	search_fields = ('universities',)
	list_filter = ('description','universities')

	def save_model(self,request,obj,form,change):
		obj.code = obj.description.replace(' ','_')
		obj.save()


class DepartmentInline(admin.TabularInline):
	model = Department
	extra = 0
	fields = ('description',)

class UniversityAdmin(admin.ModelAdmin):
	fieldsets = [
	(None, {'fields':['description','code'],
		'classes':('extrapretty',)
		}),
	]
	inlines = [DepartmentInline]

	search_fields = ('description',)

	def save_model(self,request,obj,form,change):
		obj.code = obj.description.replace(' ','_')
		obj.save()

class CourseForm(forms.ModelForm):
	
	class Meta:
		Model = Course

	def __init__(self,*args,**kwargs):
		super(CourseForm,self).__init__(*args,**kwargs)
		self.fields['prerequisite'].queryset = Course.objects.exclude(id__exact=self.instance.id)


class CourseAdmin(admin.ModelAdmin):
	form = CourseForm

admin.site.register(University,UniversityAdmin)
admin.site.register(Program)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Course,CourseAdmin)

