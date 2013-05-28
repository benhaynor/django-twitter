from django.conf.urls import patterns, url
from django.views.generic  import TemplateView

urlpatterns = patterns('twitter',
    url(r'^$','views.landing_page', name = 'home'),
    url(r'^logout$','views.logout', name = 'logout'),
    url(r'^apiclient$', TemplateView.as_view(template_name="apiclient.html")),
)
