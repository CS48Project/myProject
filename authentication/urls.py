from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^register/$', 'authentication.views.WallabyRegistration'),
	url(r'^login/$', 'authentication.views.LoginRequest'),
	url(r'^logout/$', 'authentication.views.LogoutRequest'),
)
