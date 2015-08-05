from django.conf.urls import url, patterns
from views import *

urlpatterns = [
	url(r'^$',IndexView.as_view()),
	url(r'^reports/(universities)/?$',UniversitiesView.as_view()),
	url(r'^reports/(universities)/(?P<university_id>\d+)/?$',UniversityView.as_view()),
	url(r'^reports/(programs)/(?P<program_id>\d+)/?$',ProgramView.as_view()),

]