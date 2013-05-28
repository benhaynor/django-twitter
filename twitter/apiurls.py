from django.conf.urls import patterns, include, url
from twitter.apiviews import UserTweets, TweetViews, ApiView, TweetList, UserList
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
def cors_view(f):
    def f_new(*a,**kw):
        response = f(*a,**kw)
        response['Access-Control-Allow-Origin'] = "*"
        return response
    return f_new

urlpatterns = patterns('',
    url(r'users/(\d+)/tweets',cors_view(UserTweets.as_view())),
    url(r'users/',cors_view(UserList.as_view())),
    url(r'tweets/(\d+)',cors_view(TweetViews.as_view())),
    url(r'tweets/',cors_view(TweetList.as_view())),
    url(r'^/$',cors_view(ApiView.as_view())),
)
