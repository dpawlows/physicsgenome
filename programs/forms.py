from django import forms
from django.db import models
# from django.forms import Textarea,TextInput
# from django.core.exceptions import ValidationError
from programs.models import dbUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from re import search
import pdb

def isonlyalpha(str):
    return True if search('[^A-Za-z0-9\s]',str) == None else False


class CustomUserCreationForm(UserCreationForm):
    error_css_class="error"
    required_css_class="required"

    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30,required = True)
    last_name = forms.CharField(max_length=30,required = True)
    universityAffiliation = forms.CharField(label='University Affiliation',max_length=254,required = True)

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'placeholder' : 'first name'})
        self.fields['last_name'].widget.attrs.update({'placeholder' : 'last name'})
        self.fields['email'].widget.attrs.update({'placeholder' : 'email'})
        self.fields['password1'].widget.attrs.update({'placeholder' : 'password'})
        self.fields['password2'].widget.attrs.update({'placeholder' : 'verify password'})
        self.fields['universityAffiliation'].widget.attrs.update({'placeholder' : 'university affiliation'})
        # del self.fields['username']


    class Meta:
        model = dbUser
        fields = ('email','universityAffiliation')

    # def clean_email(self):
    #   email = self.cleaned_data['email']
    #   try:
    #       User._default_manager.get(email=email)
    #   except User.DoesNotExist:
    #       return email
    #   raise forms.ValidationError('The entered email already exists.')

    def save(self,commit = True):
        user = super(CustomUserCreationForm, self).save(commit = False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.universityAffiliation = self.cleaned_data['universityAffiliation']

        if commit:
            user.save()

    #       user.save()
    #       user_profile = UserProfile(user=user)
    #       user_profile.universityAffiliation = self.cleaned_data[
    #       'universityAffiliation']
    #       user_profile.save()
        return user

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        if isonlyalpha(first_name):
            return first_name
        else:
            raise forms.ValidationError('This entry should only contain letters!')
    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        if isonlyalpha(last_name):
            return last_name
        else:
            raise forms.ValidationError('This entry should only contain letters!')




class CustomUserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(CustomUserChangeForm, self).__init__(*args, **kargs)
        # del self.fields['username']

    class Meta:
        model = dbUser
        fields = ('email',)

# class RegisterForm(forms.ModelForm):
#   error_css_class="error"
    # required_css_class="required"
#   def __init__(self, *args, **kwargs):
#       super(RegisterForm, self).__init__(*args, **kwargs)
#       self.fields['first_name'].widget.attrs.update({'class' : 'firstname'})
#       self.fields['last_name'].widget.attrs.update({'class' : 'firstname'})
#       self.fields['university'].widget.attrs.update({'class' : 'firstname'})
#       self.fields['email'].widget.attrs.update({'class' : 'firstname'})
#       self.fields['abstract'].widget.attrs.update({'class' : 'box'})
#       #self.fields['university'].required=False
#       self.fields['presentation'].label="Will you be presenting a poster?"
#       self.fields['housing'].label="Will you use EMU provided housing?"
# #     self.fields['competition'].label="Will you participate in the poster competition?"
#       self.fields['abstract'].label="If presenting, please enter your title and abstract below:"

    # class Meta:
    #   model = Person
    #   exclude = ('code','paid','checkedin')

        #widgets = {
        #'university':TextInput
        #}

#   def clean(self):

#       cleaned_data = super(RegisterForm,self).clean()

#       firstname = cleaned_data.get('first_name')
#       lastname = cleaned_data.get('last_name')
#       lenabstract = len(cleaned_data.get('abstract'))
#       presentation = cleaned_data.get('presentation')
# #     competition = cleaned_data.get('competition')


#       if Person.objects.filter(last_name=lastname).count() >= 1 and Person.objects.filter(first_name=firstname).count() >= 1:
#           raise ValidationError('This user already exists.')

#       if lenabstract == 0 and presentation:
#               raise ValidationError('You say you want to present, but you\
#                   left out your abstract!')
#       if lenabstract > 0 and not presentation:
#               cleaned_data['presentation'] = True


#           return cleaned_data

#   def clean_email(self):
#       data =  self.cleaned_data['email']
#       if Person.objects.filter(email=data).count() >= 1:
#           raise ValidationError('This email is already registered.')
#       return data
    # def clean(self):
    #   university = self.cleaned_data.get('university')
    #   new_university = self.cleaned_data.get('new_university')
    #   if not university and not new_university:
    #       raise forms.ValidationError('Please specify a university!')

    #   elif not university:
    #       university, created = University.objects.get_or_create(name=
    #           new_university)
    #       self.cleaned_data['university'] = university

    #   return super(RegisterForm,self).clean()


