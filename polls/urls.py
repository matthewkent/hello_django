from django.conf.urls import patterns, include, url

urlpatterns = patterns('polls.views',
    # Examples:
    # url(r'^$', 'hello_django.views.home', name='home'),
    # url(r'^hello_django/', include('hello_django.foo.urls')),
    url(r'^$', 'index'),
    url(r'^(?P<poll_id>\d+)/$', 'detail'),
    url(r'^(?P<poll_id>\d+)/results/$', 'results'),
    url(r'^(?P<poll_id>\d+)/vote/$', 'vote'),
)
