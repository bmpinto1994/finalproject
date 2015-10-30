from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("movie_detail", args=[self.id])

class Review(models.Model):
  movie = models.ForeignKey(Movie)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  movie = models.ForeignKey(Movie, blank=True, null=True)
  review = models.ForeignKey(Review, blank=True, null=True)

  def __unicode__(self):
    return "% upvoted" % (self.user.username)
# Create your models here.
