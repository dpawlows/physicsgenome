from django.views.generic import View, TemplateView, FormView
from django.db.models import Q
from django.template import RequestContext,loader
import models as M

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

	