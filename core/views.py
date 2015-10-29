from django.shortcuts import render
from django.views.generic import TemplateView

class Home(TemplateView):
  template_name = "home.html"

from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class MovieCreateView(CreateView):
  model = Movie
  template_name = "movie/movie_form.html"
  fields = ['title', 'description']
  success_url = reverse_lazy('movie_list')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(MovieCreateView, self).form_valid(form)

from django.views.generic import ListView

class MovieListView(ListView):
  model = Movie
  template_name = "movie/movie_list.html"

from django.views.generic import DetailView

class MovieDetailView(DetailView):
  model = Movie
  template_name = 'movie/movie_detail.html'

from django.views.generic import UpdateView

class MovieUpdateView(UpdateView):
  model = Movie
  template_name = 'movie/movie_form.html'
  fields = ['title', 'description']

# Create your views here.
