from django.db.models.signals import post_save
from django.db import models
from util import util
from django import forms
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):

    def _create_user(self, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                                 **extra_fields)


class dbUser(AbstractBaseUser,PermissionsMixin):
	email = models.EmailField(_('email'), max_length=254, unique=True)
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	last_name = models.CharField(_('last name'), max_length=30, blank=True)
	is_staff = models.BooleanField(_('staff status'), default=False,
		help_text=_('Designates whether the user can log into the admin '
			'site.'))
	is_active = models.BooleanField(_('active'), default=True,
		help_text=_('Designates whether this user should be treated as '
			'active. Unselect this instead of deleting accounts.'))
	date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
	universityAffiliation = models.CharField(_('university affiliation'),max_length=254)

	objects = CustomUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['first_name','last_name','universityAffiliation']

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		"""
		Returns the first_name plus the last_name, with a space in between.
		"""
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		"Returns the short name for the user."
		return self.first_name

	def email_user(self, subject, message, from_email=None):
		"""
		Sends an email to this User.
		"""
		send_mail(subject, message, from_email, [self.email])


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
	university = models.ForeignKey(University)
	tenured = models.IntegerField('tenure-track faculty',blank=True,null=True)
	nonTenured = models.IntegerField('non tenure-track faculty',blank=True,null=True)


	def universities_name(self):
		return self.universities

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
	description = models.CharField(max_length=80)

	def __unicode__(self):
		return '{}'.format(self.code)

class Program(models.Model):
	'''
	Programs can be physics, physics research, engineering
	physics, etc...  Should probably be set by admin.
	'''
	code = models.CharField(max_length=80,unique=True)
	description = models.CharField('program',max_length=255)
	department = models.ForeignKey(Department)


	def __unicode__(self):
		return '{}'.format(self.description)

class Course(models.Model):
	'''
	'''
	# Using code to make sure courses at different universities are unique- otherwise its easy to
	# have duplicates of a single university's course.
	# Name, description, etc don't need to be unique.

	code = models.CharField('name',max_length=80)
	courseType = models.ForeignKey(CourseType,blank=True,null=True)
	description = models.CharField(max_length=255,blank=True,null=True)
	delivery = models.ManyToManyField(Delivery,blank=True)
	content = models.ManyToManyField(Content,blank=True)
	prerequisite = models.ManyToManyField('self',blank=True,symmetrical=False)
	programs = models.ManyToManyField(Program)
	university = models.ForeignKey(University)


	class Meta:
		unique_together = ('code','university')

	def __unicode__(self):
		return '{}'.format(self.code)




















