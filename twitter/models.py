from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#A proxy model adds functionality to a class
#but does not change its database representation
class MyUser(User):
    class Meta:
        proxy = True
    
    def tweets(self):
        return Tweet.objects.filter(author__exact=self.id)

class Tweet(models.Model):
    text = models.CharField(max_length=140) 
    author = models.ForeignKey(User)

    def __unicode__(self):
        return "%s,%s" % (self.author.username, self.text)


