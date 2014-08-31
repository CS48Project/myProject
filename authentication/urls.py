"""
URLs associated with the 'authentication' app
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^register/$', 'authentication.views.user_registration'),
                       url(r'^login/$', 'authentication.views.login_request'),
                       url(r'^logout/$', 'authentication.views.logout_request'),
                       url(r'^registration_success/$', 'authentication.views.registration_success'),
                       url(r'^profile/$', 'authentication.views.profile'),
                       url(r'^password_reset/$', 'django.contrib.auth.views.password_reset', name='password_reset'),
                       url(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done',
                           name='password_reset_done'),
                       url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
                           'django.contrib.auth.views.password_reset_confirm',
                           name='password_reset_confirm'),
                       url(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete',
                           name='password_reset_complete'),
                       url(r'^votes/$', 'authentication.views.all_votes'),
                       )
