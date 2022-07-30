from django import forms
from django.forms import widgets
from webapp.models import Poll, Choice, Answer
from django.core.exceptions import ValidationError


class UserPollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]
        widgets = {
            "question": widgets.Textarea(attrs={"placeholder": "Input a question"})
        }


class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ["choice_text", "poll"]


class PollDeleteForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ["question"]

    def clean_question(self):
        question = self.cleaned_data.get("question")
        if self.instance.title != question:
            raise ValidationError("The questions do not march")
        return question


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ["choice"]
        widgets = {
            "choice": widgets.RadioSelect
        }
