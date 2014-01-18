from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^food/', include('food.urls')),
    url(r'^accounts/', include('authentication.urls')),

    url(r'^$', 'project.views.home'),
    url(r'^about/$', 'project.views.about'),
#    url(r'^profile/$', 'project.views.profile'),
    url(r'^terms/$', 'project.views.terms'),
)
