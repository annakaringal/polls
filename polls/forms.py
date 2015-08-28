from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from polls.models import Poll, Choice

ChoiceFormSet = inlineformset_factory(Poll, Choice,
                                    fields=['choice_text'],
                                    can_delete=False,
                                    extra=5)

class PollForm(ModelForm):
    class Meta:
        model = Poll
        fields = ['question',]