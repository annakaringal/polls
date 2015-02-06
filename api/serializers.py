from django.contrib.auth.models import User
from rest_framework import serializers
from polls.models import Poll, Choice

class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'groups')

class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = ('id', 'question', 'pub_date')

class ChoiceSerializer(serializers.ModelSerializer):

    poll = serializers.HyperlinkedRelatedField(read_only=True, view_name='polls-detail')

    class Meta:
        model = Choice
        fields = ('id', 'poll', 'choice_text', 'votes')
