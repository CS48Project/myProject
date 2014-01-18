from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^registration/$', 'authentication.views.WallabyRegistration'),
	url(r'^Login/$', 'authentication.views.LoginRequest'),
	url(r'^Logout/$', 'authentication.views.LogoutRequest'),
)
