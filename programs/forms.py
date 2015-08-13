from django import forms
# from django.forms import Textarea,TextInput
# from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
	error_css_class="error"
	required_css_class="required"

	email = forms.EmailField(required=True)
	first_name = forms.CharField(max_length=80,required = False)
	last_name = forms.CharField(max_length=80,required = False)
	university_affil = forms.CharField(max_length=80,required = True)

	class Meta:
		model = User
		fields = ('username','email','password1','password2')

	def save(self,commit = True):
		user = super(RegisterForm, self).save(commit = False)
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.university_affil = self.cleaned_data['university_affil']

		if commit:
			user.save()

		return user



# class RegisterForm(forms.ModelForm):
# 	error_css_class="error"
	# required_css_class="required"
# 	def __init__(self, *args, **kwargs):
# 		super(RegisterForm, self).__init__(*args, **kwargs)
# 		self.fields['first_name'].widget.attrs.update({'class' : 'firstname'})
# 		self.fields['last_name'].widget.attrs.update({'class' : 'firstname'})
# 		self.fields['university'].widget.attrs.update({'class' : 'firstname'})
# 		self.fields['email'].widget.attrs.update({'class' : 'firstname'})
# 		self.fields['abstract'].widget.attrs.update({'class' : 'box'})
# 		#self.fields['university'].required=False
# 		self.fields['presentation'].label="Will you be presenting a poster?"
# 		self.fields['housing'].label="Will you use EMU provided housing?"
# #		self.fields['competition'].label="Will you participate in the poster competition?"
# 		self.fields['abstract'].label="If presenting, please enter your title and abstract below:"

	# class Meta:
	# 	model = Person
	# 	exclude = ('code','paid','checkedin')

		#widgets = {
		#'university':TextInput
		#}

# 	def clean(self):

# 		cleaned_data = super(RegisterForm,self).clean()

# 		firstname = cleaned_data.get('first_name')
# 		lastname = cleaned_data.get('last_name')
# 		lenabstract = len(cleaned_data.get('abstract'))
# 		presentation = cleaned_data.get('presentation')
# #		competition = cleaned_data.get('competition')


# 		if Person.objects.filter(last_name=lastname).count() >= 1 and Person.objects.filter(first_name=firstname).count() >= 1:
# 		 	raise ValidationError('This user already exists.')
		
# 	   	if lenabstract == 0 and presentation:
# 	   	 		raise ValidationError('You say you want to present, but you\
# 	   	 			left out your abstract!')
# 	   	if lenabstract > 0 and not presentation:
# 	   	 		cleaned_data['presentation'] = True
   	 	
   	 	
#    	 	return cleaned_data
	
# 	def clean_email(self):
# 		data =  self.cleaned_data['email']
# 		if Person.objects.filter(email=data).count() >= 1:
# 			raise ValidationError('This email is already registered.')
# 		return data
	# def clean(self):
	# 	university = self.cleaned_data.get('university')
	# 	new_university = self.cleaned_data.get('new_university')
	# 	if not university and not new_university:
	# 		raise forms.ValidationError('Please specify a university!')

	# 	elif not university:
	# 		university, created = University.objects.get_or_create(name=
	# 			new_university)
	# 		self.cleaned_data['university'] = university

	# 	return super(RegisterForm,self).clean()

