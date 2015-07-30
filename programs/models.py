
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

class CourseType(models.Model):
	code = models.CharField(max_length=80)

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
	

	def __unicode__(self):
		return '{}'.format(self.description)

class Course(models.Model):
	'''
	'''
	# Using code to make sure courses at different universities are unique- otherwise its easy to 
	# have duplicates of a single university's course.
	# Name, description, etc don't need to be unique.

	code = models.CharField(max_length=80,unique=True)
	courseType = models.ForeignKey(CourseType,blank=True,null=True)
	name = models.CharField(max_length=80)
	description = models.CharField(max_length=255,blank=True,null=True)
	delivery = models.ManyToManyField(Delivery,blank=True)
	content = models.ManyToManyField(Content,blank=True)
	contentType = models.ManyToManyField(ContentType,blank=True)
	prerequisite = models.ManyToManyField('self',blank=True,symmetrical=False)
	programs = models.ManyToManyField(Program)
	university = models.ForeignKey(University)

		
	class Meta:
		unique_together = ('code','university')

	def __unicode__(self):
		return '{}'.format(self.name)




















