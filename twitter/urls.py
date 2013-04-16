from django.conf.urls import patterns, url
from twitter.views import TweetDetail

urlpatterns = patterns('twitter',
    url(r'^$','views.landing_page', name = 'home'),
    url(r'^logout$','views.logout', name = 'logout'),
    url(r'^tweets/(?P<pk>\d+)/$', TweetDetail.as_view(), name='meal-detail'),
)
