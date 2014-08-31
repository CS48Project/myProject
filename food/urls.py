"""
URLs associated with the 'food' app
"""

from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^$', 'food.views.food_index'),
                       url(r'^(?P<foodslug>.*)/(?P<food_id>\d+)/$', 'food.views.food'),
                       url(r'^submit/$', 'food.views.submit'),
                       url(r'^(?P<foodslug>.*)/(?P<food_id>\d+)/edit/$', 'food.views.edit'),
                       url(r'^foodoftheday/$', 'food.views.food_of_the_day'),
                       url(r'^whattoeat/$', 'food.views.what_to_eat'),
                       url(r'^categories/$', 'food.views.category_index'),
                       url(r'^categories/(?P<categoryslug>.*)/$', 'food.views.category'),
                       url(r'^restaurants/$', 'food.views.restaurant_index'),
                       url(r'^restaurants/(?P<restaurantslug>.*)/$', 'food.views.restaurant'),
                       url(r'^submitsuccess/$', 'food.views.submit_success'),
                       )
