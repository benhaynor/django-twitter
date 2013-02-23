from django.conf.urls import patterns, url

urlpatterns = patterns('twitter',
    url(r'^$','views.landing_page'),
    url(r'^register$','views.register'),
    url(r'^login','views.login_view') 
)
