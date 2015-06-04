from django.db import models


class Universities(models.Model):
	'''
	Tracking the name.  Can be used later for 
	other stuff.  
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
        return '{}'.format(self.description)


class Departments(models.Model):
	'''
	Mostly Physics.  Maybe something else.  Really 
	a container for faculty.
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)


	def __unicode__(self):
        return '{}'.format(self.description)


class Faculty(models.Model):
	'''
	I think this should be its own class.  These
	will be set by admin for more accurate tracking.
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.Charfield(max_length=255)

	def __unicode__(self):
		return '{}'.format(self.description)

class DepartmentHasFaculty(models.Model):
	'''
	'''
	department = models.ForeignKey(Department)
	faculty = models.ForeignKey(Faculty)


class Programs(models.Model):
	'''
	Programs can be physics, physics research, engineering
	physics, etc...
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)

	def __unicode__(self):
        return '{}'.format(self.description)


class Courses(models.Model):
	'''
	How do we handle this?  Do we try to have 1 class for
	sophomore physics?  That doesn't seem right...
	'''

	code = models.CharField(max_length=80,unique=True)
	description = models.CharFiled(max_length=255)

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



