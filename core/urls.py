from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
                      url(r'^$', Home.as_view(), name='home'),
                       url(r'^user/', include('registration.backends.simple.urls')),
                       url(r'^user/', include('django.contrib.auth.urls')),
                       url(r'^movie/create/$', login_required(MovieCreateView.as_view()), name='movie_create'),
                       url(r'movie/$', login_required(MovieListView.as_view()), name='movie_list'),
                       url(r'^movie/(?P<pk>\d+)/$', login_required(MovieDetailView.as_view()), name='movie_detail'),
                       url(r'^movie/update/(?P<pk>\d+)/$', login_required(MovieUpdateView.as_view()), name='movie_update'),
                       url(r'^movie/delete/(?P<pk>\d+)/$', login_required(MovieDeleteView.as_view()), name='movie_delete'),
                       url(r'^movie/(?P<pk>\d+)/review/create/$', login_required(ReviewCreateView.as_view()), name='review_create'),
                       url(r'^movie/(?P<movie_pk>\d+)/review/update/(?P<review_pk>\d+)/$', login_required(ReviewUpdateView.as_view()), name='review_update'),
                       url(r'^movie/(?P<movie_pk>\d+)/review/delete/(?P<review_pk>\d+)/$', login_required(ReviewDeleteView.as_view()), name='review_delete'),
                       url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),
                       url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
                       url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
                       url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
                      )