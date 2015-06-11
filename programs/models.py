
from django.db import models
from util import util

class Department(models.Model):
	'''
	This should be populated by admin?
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)
	

	def __unicode__(self):
		return '{}'.format(self.description)

	
class Program(models.Model):
	'''
	Programs can be physics, physics research, engineering
	physics, etc...  Should probably be set by admin.
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)

class Faculty(models.Model):
	'''

	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)
 
	class Meta:
		verbose_name_plural = "Faculty"

class Course(models.Model):
	'''
	How do we handle this?  Do we try to have 1 class for
	sophomore physics?  That doesn't seem right...
	'''

	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.code)


class Content(models.Model):
	'''
	This might get ugly and difficult to track if we don't
	limit the entries.
	'''

	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)

	class Meta:
		verbose_name_plural = "Content"

class ContentType(models.Model):
	'''
	Something like math, experimental physics, 
	theory, computational
	'''

	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)

class Delivery(models.Model):
	'''
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)
	def __unicode__(self):
		return '{}'.format(self.description)

class University(models.Model):
	'''
	
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)
	departments = models.ManyToManyField(Department)
	programs = models.ManyToManyField(Program,through='UniversityHasProgram')
	courses = models.ManyToManyField(Course,through='UniversityHasCourse')
	faculty = models.ManyToManyField(Faculty,through='UniversityHasFaculty')
	content = models.ManyToManyField(Content,through='UniversityHasContent')
	

	def __unicode__(self):
		return '{}'.format(self.description)

	class Meta:
		verbose_name_plural = "Universities"



class UniversityHasFaculty(models.Model):
	'''
	'''
	university = models.ForeignKey(University)
	department = models.ForeignKey(Department)
	faculty = models.ForeignKey(Faculty)
	number = models.IntegerField()

	def __unicode__(self):
		return '{}'.format(self.description)


class UniversityHasProgram(models.Model):
	university = models.ForeignKey(University)
	department = models.ForeignKey(Department)
	program = models.ForeignKey(Program)

	def __unicode__(self):
		return '{}'.format(self.university)

class UniversityHasCourse(models.Model):
	university = models.ForeignKey(University)
	course = models.ForeignKey(Course)
	department = models.ForeignKey(Department)
	program = models.ForeignKey(Program)
	
	delivery = models.ForeignKey(Delivery)

	def __unicode__(self):
		return '{},{}'.format(self.university,self.program)


class UniversityHasContent(models.Model):
	university = models.ForeignKey(University)
	course = models.ForeignKey(Course)
	content = models.ForeignKey(Content)
	content_type = models.ForeignKey(ContentType)

	def __unicode__(self):
		return '{},{}'.format(self.university,self.course)





