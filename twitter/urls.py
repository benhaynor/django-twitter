from django.conf.urls import patterns, url

urlpatterns = patterns('twitter',
    url(r'^$','views.landing_page', name = 'home'),
    url(r'^logout$','views.logout', name='logout')
)
