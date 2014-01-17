from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^all/$', 'food.views.food_index'),
	url(r'^get/(?P<food_id>\d+)/$', 'food.views.food'),
	url(r'^submit/$', 'food.views.create'),
)
