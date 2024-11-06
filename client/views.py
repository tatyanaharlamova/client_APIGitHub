from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from client.models import Git, Commit


class CommitListView(ListView):
    model = Commit


class GitDetailView(DetailView):
    model = Git


class GitCreateView(CreateView):
    model = Git
    success_url = reverse_lazy('client:git_detail')
    fields = ['name']


class CommitCreateView(CreateView):
    model = Commit
    success_url = reverse_lazy('client:commit_list')
