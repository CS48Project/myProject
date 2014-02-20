from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'food.views.food_index'),
	url(r'^categories/(?P<categoryslug>.*)/(?P<foodslug>.*)/(?P<food_id>\d+)/$', 'food.views.food'),
	url(r'^submit/$', 'food.views.submit'),
	url(r'^foodoftheday/$', 'food.views.food_of_the_day'),
    url(r'^whattoeat/$', 'food.views.what_to_eat'),
    url(r'^categories/$', 'food.views.category_index'),
    url(r'^categories/(?P<categoryslug>.*)/$', 'food.views.category'),
    url(r'^submitsuccess/$', 'food.views.submit_success'),
    url(r'^search/$', 'food.views.search_food'),
)
