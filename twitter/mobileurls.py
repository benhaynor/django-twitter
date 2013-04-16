from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^/$','twitter.mobileviews.hello'),
    url('^/discover/$','twitter.mobileviews.discover'),
    url('/home/$','twitter.views.landing_page'),
    url('^/me/$','twitter.mobileviews.me'),
    url('^/content/$','twitter.mobileviews.content'),
    url('^/newtweet/$','twitter.mobileviews.newtweet'),
)

