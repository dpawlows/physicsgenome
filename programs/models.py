
from django.db import models
from util import util

class University(models.Model):
	'''
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField('name',max_length=255) #Added name as verbose_name

	def __unicode__(self):
		return '{}'.format(self.description)

	class Meta:
		verbose_name_plural = "Universities"

class Department(models.Model):
	'''
	
	'''
	code = models.CharField(max_length=80)
	description = models.CharField('name',max_length=255) #verbose_name
	universities = models.ForeignKey(University)
	
	def universities_name(self):
		return self.universities

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

class ContentType(models.Model):
	'''
	Something like math, experimental physics, 
	theory, computational
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
	content_type = models.ManyToManyField(ContentType)

	def __unicode__(self):
		return '{}'.format(self.description)

	class Meta:
		verbose_name_plural = "Content"


class Delivery(models.Model):
	'''
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
	delivery = models.ManyToManyField(Delivery)
	content = models.ManyToManyField(Content)
	contentType = models.ManyToManyField(ContentType)
	prerequisite = models.ManyToManyField('self')
	


	def __unicode__(self):
		return '{}'.format(self.code)

class Program(models.Model):
	'''
	Programs can be physics, physics research, engineering
	physics, etc...  Should probably be set by admin.
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField(max_length=255)
	departments = models.ForeignKey(Department)
	courses = models.ManyToManyField(Course)

	def __unicode__(self):
		return '{}'.format(self.description)


















