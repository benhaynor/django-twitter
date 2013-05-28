from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#A proxy model adds functionality to a class
#but does not change its database representation
class Tweeter(models.Model):

    user = models.OneToOneField(User)
    following = models.ManyToManyField("self")

    @property
    def tweets(self):
        return Tweet.objects.filter(author__exact=self.id).order_by('-created')

    @property
    def suggested_friends(self):
        return Tweeter.objects.exclude(id__exact=self.id)[:3]

    def serialized(self):
        json_rep = {}
        json_rep['username'] = self.user.username
        json_rep['tweets'] = '/user/%d/tweets' % self.id
        return json_rep

class Tweet(models.Model):
    text = models.CharField(max_length=140) 
    author = models.ForeignKey(Tweeter)
    created = models.DateTimeField(auto_now=True)

    @property
    def author_user(self):
        return self.auther.user

    def __unicode__(self):
        return "%s,%s" % (self.author.username, self.text)

    def serialized(self):
        json_rep = {k:str(getattr(self,k)) for k in ('text', 'created')}
        json_rep['author'] = '/users/%d' % self.author.id
        return json_rep
