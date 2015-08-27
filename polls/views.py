from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.views import generic

from .models import Choice, Poll, Vote
from django.contrib.auth.models import User


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_poll_list'

    def get_queryset(self):
        """
        Return the last five published polls (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]

class AllView(generic.ListView):
    template_name = 'polls/all.html'

    def get_queryset(self):
        """
        Return all existing (not including those set to be
        published in the future).
        """
        return Poll.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')

class AnsweredView(generic.ListView):
    template_name = 'polls/answered.html'
    context_object_name = 'user_list'

    def get_queryset(self):
        """
        Return all users who have submitted polls
        """
        return User.objects.exclude(
            vote__isnull=True
        )

class DetailView(generic.DetailView):
    model = Poll
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any polls that aren't published yet.
        """
        return Poll.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Poll
    template_name = 'polls/results.html'


def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        if request.user.is_authenticated():
            if Vote.objects.filter(user=request.user, poll=p).exists():
                return render(request, 'polls/detail.html', {
                                'poll': p,
                                'error_message': "You have already voted in this poll",
                            })
            else: 
                selected_choice.votes += 1
                selected_choice.save()
                vote = Vote(user=request.user, poll=p, choice=selected_choice)
                vote.save()
                # Always return an HttpResponseRedirect after successfully dealing
                # with POST data. This prevents data from being posted twice if a
                # user hits the Back button.
                return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
        else:
            return render(request, 'polls/detail.html', {
                'poll': p,
                'error_message': "You must be logged in to vote",
            })


class pollsAngularApp(generic.TemplateView):
    template_name = 'base.html'
