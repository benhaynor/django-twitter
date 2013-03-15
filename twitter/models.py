from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#A proxy model adds functionality to a class
#but does not change its database representation
class Tweeter(models.Model):

    user = models.OneToOneField(User)

    @property
    def tweets(self):
        return Tweet.objects.filter(author__exact=self.id).order_by('-created')

class Tweet(models.Model):
    text = models.CharField(max_length=140) 
    author = models.ForeignKey(Tweeter)
    created = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%s,%s" % (self.author.username, self.text)
