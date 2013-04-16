from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('twitter.mobileviews',
    url('^/$','hello'),
    url('^/discover/$','discover'),
    url('/home/$','home'),
    url('^/me/$','me'),
    url('^/content/$','content'),
)

