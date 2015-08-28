from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^all/$', views.AllView.as_view(), name='all'),
    url(r'^answered/$', views.AnsweredView.as_view(), name='answered'),
    url(r'^new/$', views.new, name='new'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<poll_id>\d+)/add/$', views.add, name='add'),
)
