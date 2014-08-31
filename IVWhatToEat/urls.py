"""
Site-wide URLs
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',

                       # Include external URLs from the various apps.
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^food/', include('food.urls')),
                       url(r'^accounts/', include('authentication.urls')),
                       url(r'^ratings/', include('ratings.urls')),
                       url(r'^comments/', include('django_comments.urls')),
                       url(r'^search/', include('haystack.urls')),

                       # Define site-wide URLs (not associated with any particular app).
                       url(r'^$', 'IVWhatToEat.views.home'),
                       url(r'^about/$', 'IVWhatToEat.views.about'),
                       url(r'^terms/$', 'IVWhatToEat.views.terms'),
                       )
