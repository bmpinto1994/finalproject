from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
                      url(r'^$', Home.as_view(), name='home'),
                       url(r'^user/', include('registration.backends.simple.urls')),
                       url(r'^user/', include('django.contrib.auth.urls')),
                       url(r'^movie/create/$', MovieCreateView.as_view(), name='movie_create'),
                       url(r'movie/$', MovieListView.as_view(), name='movie_list'),
                       url(r'^movie/(?P<pk>\d+)/$', MovieDetailView.as_view(), name='movie_detail'),
                       url(r'^movie/update/(?P<pk>\d+)/$', MovieUpdateView.as_view(), name='movie_update'),
                       url(r'^movie/delete/(?P<pk>\d+)/$', MovieDeleteView.as_view(), name='movie_delete'),
                       url(r'^movie/(?P<pk>\d+)/review/create/$', ReviewCreateView.as_view(), name='review_create'),
                      )