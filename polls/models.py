import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Poll(models.Model):
    question = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.question

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date < now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):  # Python 3: def __str__(self):
        return self.choice_text

class Vote(models.Model):
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(default=datetime.datetime.now)

    def __unicode__(self): 
        return unicode(self.choice)