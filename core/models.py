RATING_CHOICES = (
(0, 'None'),
(1, '*'),
(2, '**'),
(3, '***'),
(4, '****'),
(5, '*****'),
)

from django.core.urlresolvers import reverse
VISABILITY_CHOICES = (
(0, 'Public'),
(1, 'Anonymous'),
)
from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
  title = models.CharField(max_length=300)
  description = models.TextField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(User)
  visability = models.IntegerField(choices=VISABILITY_CHOICES, default=0)

  def __unicode__(self):
    return self.title

  def get_absolute_url(self):
    return reverse("movie_detail", args=[self.id])

class Review(models.Model):
  movie = models.ForeignKey(Movie)
  user = models.ForeignKey(User)
  created_at = models.DateTimeField(auto_now_add=True)
  text = models.TextField()
  visability = models.IntegerField(choices=VISABILITY_CHOICES, default=0)
  rating = models.IntegerField(choices=RATING_CHOICES, default=0)

  def __unicode__(self):
    return self.text

class Vote(models.Model):
  user = models.ForeignKey(User)
  movie = models.ForeignKey(Movie, blank=True, null=True)
  review = models.ForeignKey(Review, blank=True, null=True)

  def __unicode__(self):
    return "% upvoted" % (self.user.username)
# Create your models here.
