from django.contrib.admin import TabularInline, StackedInline, site
from super_inlines.admin import SuperModelAdmin,SuperInlineModelAdmin
from django import forms
from programs.models import *
from programs.util.util import chopr

import pdb

class ProgramAdmin(SuperModelAdmin):

	# fieldsets = [
	# (None,{'fields':['description','departments.universities']}),
	# ]
	list_display = ('description','get_university')
	search_fields=('description','department__university__code')
	list_filter = ('department__university',)
	def get_university(self,obj):
		return obj.department.university
	get_university.short_description = 'University'

class ProgramInline(SuperInlineModelAdmin,TabularInline):
	model = Program
	# extra = 3

class DepartmentAdmin(SuperModelAdmin):

	fieldsets = [
	(None, {'fields':['description','university']}),
	]
	list_display = ('description','university',)
	inlines = [ProgramInline]

	search_fields = ('university__description','description')
	list_filter = ('description','university')

	def save_model(self,request,obj,form,change):
		obj.code = obj.description.replace(' ','_')
		obj.save()


class DepartmentInline(SuperInlineModelAdmin,StackedInline):
	model = Department
	extra = 0
	fields = ('description',)

	inlines = (ProgramInline,)

class UniversityAdmin(SuperModelAdmin):
	fieldsets = [
	(None, {'fields':['description','code'],
		'classes':('extrapretty',)
		}),
	]
	inlines = [DepartmentInline,]

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

	def clean(self):
		cleaned_data = self.cleaned_data
		if Course.objects.filter(code=cleaned_data['code'],university=cleaned_data['university']).exists():
			raise forms.ValidationError('The course already exists at this university.')
			# pdb.set_trace()	

		return cleaned_data

class CourseAdmin(SuperModelAdmin):
	form = CourseForm

	list_display = ('code','university',)
	list_filter = ('university',)
	search_fields = ('code',)

	def save_model(self,request,obj,form,change):
		if obj.code == '':
			# newid = chopr('000'+str(obj.university.id),3)
			obj.code = obj.name.replace(' ','_')

		obj.save()



site.register(University,UniversityAdmin)
site.register(Program,ProgramAdmin)
site.register(Department,DepartmentAdmin)
site.register(Course,CourseAdmin)

