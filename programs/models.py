from django.db import models
from util import savecode

class Department(models.Model):
	'''
	This should be populated by admin?
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)

	

class Universities(models.Model):
	'''
	Tracking the name.  Can be used later for 
	other stuff.  
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)
	department = models.ManyToManyField(Department,through='DepartmentHasUniversity')
	def __unicode__(self):
		return '{}'.format(self.description)

	class Meta:
		verbose_name_plural = "Universities"


class DepartmentHasUniversity(models.Model):
	department = models.ForeignKey(Department)
	university = models.ForeignKey(Universities)
	def __unicode__(self):
		return '{}'.format(self.university)
		
class Faculty(models.Model):
	'''

	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)
	department = models.ForeignKey(Universities)
	university = models.ForeignKey(Department)

	def __unicode__(self):
		return '{}'.format(self.description)
 
	class Meta:
		verbose_name_plural = "Faculty"

# class DepartmentHasFaculty(models.Model):
# 	'''
# 	'''
# 	department = models.ForeignKey(Department)
	# faculty = models.ForeignKey(Faculty)


class Program(models.Model):
	'''
	Programs can be physics, physics research, engineering
	physics, etc...
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)


class Course(models.Model):
	'''
	How do we handle this?  Do we try to have 1 class for
	sophomore physics?  That doesn't seem right...
	'''

	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)


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

class ProgramHasCourse(models.Model):
	program = models.ForeignKey(Program)

	def __unicode__(self):
		return '{}'.format(self.program)



