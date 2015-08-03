from django.conf.urls import url, patterns
from views import *

urlpatterns = [
	url(r'^$',IndexView.as_view()),
	url(r'^reports/(universities)/?$',UniversitiesView.as_view()),
]