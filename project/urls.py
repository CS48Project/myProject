from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'project.views.home'),
    url(r'^whattoeat/$', 'project.views.what_to_eat'),
    url(r'^foodoftheday/$', 'project.views.food_of_the_day'),
    url(r'^submit/$', 'project.views.submit'),
    url(r'^index/$', 'project.views.index'),
    url(r'^register/$', 'project.views.register'),
    url(r'^login/$', 'project.views.login'),
    url(r'^profile/$', 'project.views.profile'),
)
