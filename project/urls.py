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

    # Define site-wide URLs (not associated with any particular app).
    url(r'^$', 'project.views.home'),
    url(r'^about/$', 'project.views.about'),
    url(r'^terms/$', 'project.views.terms'),
)
