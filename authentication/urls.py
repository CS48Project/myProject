"""
URLs associated with the 'authentication' app
"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^register/$', 'authentication.views.UserRegistration'),
	url(r'^login/$', 'authentication.views.LoginRequest'),
	url(r'^logout/$', 'authentication.views.LogoutRequest'),
	url(r'^registrationsuccess/$', 'authentication.views.registrationsuccess'),
	url(r'^profile/$', 'authentication.views.profile'),
)
