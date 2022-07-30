from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ChoiceForm
from webapp.models import Poll, Choice


class CreateChoice(CreateView):
    form_class = ChoiceForm
    template_name = "choices/create.html"

    def form_valid(self, form):
        poll = get_object_or_404(Poll, pk=self.kwargs.get("pk"))
        form.instance.poll = poll
        print(form.instance)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class UpdateChoice(UpdateView):
    form_class = ChoiceForm
    template_name = "choices/update.html"
    model = Choice

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})


class DeleteChoice(DeleteView):
    model = Choice

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("poll_view", kwargs={"pk": self.object.poll.pk})
