from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy

# Create your views here.
from django.utils.http import urlencode

from webapp.forms import PollForm, PollDeleteForm, UserPollForm
from webapp.models import Poll, Choice
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class IndexView(ListView):
    model = Poll
    template_name = "polls/index.html"
    context_object_name = "polls"
    ordering = "-created_at"
    paginate_by = 5

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Poll.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class PollView(DetailView):
    template_name = "polls/poll_view.html"
    model = Poll

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.object.id
        print(id)
        context['choices'] = Choice.objects.filter(poll_id=id)
        return context


class CreatePoll(CreateView):
    form_class = PollForm
    template_name = "polls/create.html"

    def form_valid(self, form):
        poll = form.save(commit=False)
        poll.save()
        form.save_m2m()
        return redirect("poll_view", pk=poll.pk)


class UpdatePoll(UpdateView):
    form_class = PollForm
    template_name = "polls/update.html"
    model = Poll

    def get_form_class(self):
        if self.request.GET.get("is_admin"):
            return PollForm
        return UserPollForm


class DeletePoll(DeleteView):
    model = Poll
    template_name = "polls/delete.html"
    success_url = reverse_lazy('index')
    form_class = PollDeleteForm

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST, instance=self.get_object())
        if form.is_valid():
            return self.delete(request, *args, **kwargs)
        else:
            return self.get(request, *args, **kwargs)
