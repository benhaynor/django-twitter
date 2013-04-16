from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url('^/$','twitter.mobileviews.main'),
    url('^/sign_in_success/$','twitter.mobileviews.sign_in_success'),
    url('^/sign_up_success/$','twitter.mobileviews.sign_up_success'),
    url('^/discover/$','twitter.mobileviews.discover'),
    url('/home/$','twitter.views.landing_page'),
    url('^/me/$','twitter.mobileviews.me'),
    url('^/newtweet/$','twitter.mobileviews.newtweet'),
)

