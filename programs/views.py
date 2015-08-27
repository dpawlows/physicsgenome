from django.views.generic import View, TemplateView, FormView
from django.db.models import Q
from django.template import RequestContext,loader
from django.shortcuts import render_to_response, get_object_or_404
from django.core.context_processors import csrf
from .forms import RegistrationForm
import models as M
import operator
import pdb

class IndexView(TemplateView):
	template_name = 'index.html'

class UniversitiesView(TemplateView):
	template_name = 'reports/universities.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		context.update(dict(universities=M.University.objects.all().order_by('description')))

		return self.render_to_response(context)

class UniversityView(TemplateView):
	template_name = 'reports/university.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		university = M.University.objects.get(pk=kwargs['university_id'])
		departments = M.Department.objects.filter(university__id=university.id)

		context.update(dict(
			university=university,
			departments=self.get_departmentInfo(departments)
			))

		return self.render_to_response(context)

	def get_departmentInfo(self,departments):
		#Need all programs from all departments at the university.  Don't know how many departments!
	
		predicates = [('department__id',x.id) for x in departments] 
		query_list = [Q(pred) for pred in predicates]
		result = []
		for i in range(len(departments)):
			result.append(dict(
				department=departments[i],
				programs=M.Program.objects.filter(query_list[i]),
				))

		
		return result	
		# return M.Program.objects.filter(reduce(operator.or_, query_list))

class ProgramView(TemplateView):
	template_name = 'reports/program.html'

	def get(self, request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		program = M.Program.objects.get(pk=kwargs['program_id'])
		courses = M.Course.objects.filter(programs__id=program.id)

		context.update(dict(
			program=program,
			courses=courses,
			))



		return self.render_to_response(context)


class RegisterView(TemplateView):
	template_name = 'registration_success.html'


	def render(self,request,form):
		context = RequestContext(request,{'title': 'Register','form':form})
		return render_to_response('register.html',context)

	def post(self,request,*args,**kwargs):
		form = RegistrationForm(request.POST)
		# pdb.set_trace()
		if form.is_valid():
			user, user_profile = form.save()
			context = self.get_context_data(**kwargs)
			context.update(dict(user=user,user_profile=user_profile
				))
			return self.render_to_response(context)
		else:
			return self.render(request,form)

	def get(self,request,*args,**kwargs):
		form = RegistrationForm()
		# pdb.set_trace()
		return self.render(request,form)



class RegistrationSuccess(TemplateView):
	template_name='registration_success.html'

	def get(self,request, *args, **kwargs):
		context = self.get_context_data(**kwargs)
		# pdb.set_trace()
		user = User.objects.get(pk=kwargs('user_id'))

		return self.render_to_response(context)
