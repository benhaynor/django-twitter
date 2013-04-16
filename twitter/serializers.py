from rest_framework import serializers
from twitter.models import Tweet

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet


