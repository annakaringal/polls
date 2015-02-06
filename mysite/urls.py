from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from api import views
from django.conf import settings
from polls.views import pollsAngularApp

router = routers.DefaultRouter()
router.register(r'polls', views.PollsViewSet, base_name='polls')
router.register(r'choices', views.ChoiceViewSet, base_name='choices')
router.register(r'users', views.UserViewSet, base_name='users')
admin.autodiscover()

urlpatterns = patterns('',
                       (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                       url(r'^polls/', include('polls.urls', namespace="polls")),
                       url(r'^polls_app/', pollsAngularApp.as_view()),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(router.urls)),
                       )
