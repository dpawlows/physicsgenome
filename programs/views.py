from django.views.generic import View, TemplateView, FormView
from django.db.models import Q
from django.template import RequestContext,loader
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
			departments=departments,
			programs=self.get_programs(departments)
			))

		return self.render_to_response(context)

	def get_programs(self,departments):
		#Need all programs from all departments at the university.  Don't know how many departments!
	
		predicates = [('department__id',x.id) for x in departments] 
		query_list = [Q(pred) for pred in predicates]

		return M.Program.objects.filter(reduce(operator.or_, query_list))

