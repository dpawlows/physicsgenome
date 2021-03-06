from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django import forms
from programs.models import *
from programs.forms import CustomUserCreationForm, CustomUserChangeForm
import pdb

class ProgramAdmin(admin.ModelAdmin):

	list_display = ('description','get_university')
	search_fields=('description','department__university__code')
	list_filter = ('department__university',)

	def get_university(self,obj):
		return obj.department.university

	def save_model(self,request,obj,form,change):
		obj.code = obj.description.replace(' ','_')
		obj.save()

	get_university.short_description = 'University'

	def change_view(self,request,object_id,extra_content=None):
		self.exclude = ('',)
		return super(ProgramAdmin,self).change_view(request,object_id)

	def add_view(self,request,extra_content=None):

		self.exclude = ('code',)
		return super(ProgramAdmin,self).add_view(request)

class ProgramInline(admin.TabularInline):
	model = Program
	extra = 0
	fields = ('description',)

class DepartmentAdmin(admin.ModelAdmin):

	fieldsets = [
	(None, {'fields':['description','university','tenured','nonTenured']}),
	]
	inlines = [ProgramInline]

	search_fields = ('university__description','description')
	list_filter = ('description','university')

	def save_model(self,request,obj,form,change):
		if obj.code == '':
			obj.code = obj.name.replace(' ','_')
		obj.save()


class DepartmentInline(admin.TabularInline):
	model = Department
	extra = 0
	fields = ('description',)

class UniversityAdmin(admin.ModelAdmin):

	inlines = [DepartmentInline]

	search_fields = ('description',)

	def save_model(self,request,obj,form,change):
		obj.code = obj.description.replace(' ','_')
		obj.save()

	def change_view(self,request,object_id,extra_content=None):
		self.exclude = ('',)
		return super(UniversityAdmin,self).change_view(request,object_id)

	def add_view(self,request,extra_content=None):

		self.exclude = ('code',)
		return super(UniversityAdmin,self).add_view(request)


class CourseForm(forms.ModelForm):

	class Meta:
		Model = Course

	def __init__(self,*args,**kwargs):
		super(CourseForm,self).__init__(*args,**kwargs)
		self.fields['prerequisite'].queryset = Course.objects.exclude(id__exact=self.instance.id)

	def clean(self):
		#Need to handle validation for unique_together

		cleaned_data = self.cleaned_data
		if self.instance.pk is None:
			if Course.objects.filter(code=cleaned_data['code'],university=cleaned_data['university']).exists():
				raise forms.ValidationError('The course already exists at this university.')

		return cleaned_data

class CourseAdmin(admin.ModelAdmin):
	form = CourseForm

	list_display = ('code','university',)
	list_filter = ('university',)
	search_fields = ('code',)

	def save_model(self,request,obj,form,change):
		if obj.code == '':
			obj.code = obj.name.replace(' ','_')

		obj.save()


class dbAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		(_('Personal info'), {'fields': ('first_name', 'last_name')}),
		(_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
			'groups', 'user_permissions')}),
		(_('Important dates'), {'fields': ('last_login', 'date_joined')}),
		)

	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2')}
			),
		)
	form = CustomUserChangeForm
	add_form = CustomUserCreationForm
	list_display = ('email', 'first_name', 'last_name', 'is_staff')
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('email',)

admin.site.register(dbUser, dbAdmin)
admin.site.register(University,UniversityAdmin)
admin.site.register(Program,ProgramAdmin)
admin.site.register(Department,DepartmentAdmin)
admin.site.register(Course,CourseAdmin)

