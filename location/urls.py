from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^$', 'location.views.home'),
)
