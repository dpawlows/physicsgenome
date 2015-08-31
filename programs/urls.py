from django.conf.urls import url, patterns
from views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
	url(r'^$',IndexView.as_view()),
	url(r'^reports/(universities)/?$',UniversitiesView.as_view()),
	url(r'^reports/(universities)/(?P<university_id>\d+)/?$',UniversityView.as_view()),
	url(r'^reports/(programs)/(?P<program_id>\d+)/?$',ProgramView.as_view()),
	url(r'^register/?$',RegisterView.as_view()),
	url(r'^registration_success/(P<user_id>\d+)/?$',RegistrationSuccess.as_view()),
    url(r'^login/$', 'django.contrib.auth.views.login',name='login',kwargs={'template_name':'registration/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()