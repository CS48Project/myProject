from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'food.views.food_index'),
	url(r'^(?P<food_id>\d+)/$', 'food.views.food'),
	url(r'^submit/$', 'food.views.submit'),
	url(r'^foodoftheday/$', 'food.views.food_of_the_day'),
    url(r'^whattoeat/$', 'food.views.what_to_eat'),
    url(r'^categories/$', 'food.views.category_index'),
)
