from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import AnswerForm
from webapp.models import Poll, Choice, Answer


class CreateAnswer(CreateView):
    form_class = AnswerForm
    template_name = "answers/create.html"

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.poll = poll
        print(form.instance)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        context['poll_data'] = poll
        return context

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class UpdateAnswer(UpdateView):
    form_class = AnswerForm
    template_name = "answers/update.html"
    model = Answer

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class DeleteAnswer(DeleteView):
    model = Choice

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})
