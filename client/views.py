from django.urls import reverse_lazy
from django.views.generic import ListView,  CreateView
from github import Github

from client.forms import GitForm
from client.models import Git, Commit


class CommitListView(ListView):
    model = Commit
    ordering = ['-date']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_value = self.request.GET.get("search", False)
        if search_value:

            objects = Commit.objects.filter(comments=search_value)
            context['object_list'] = objects
            context['search'] = search_value
        return context


class GitListView(ListView):
    model = Git

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        git = Git.objects.all().order_by('-id').first()
        context_data['git'] = git

        return context_data


class GitCreateView(CreateView):
    model = Git
    form_class = GitForm
    success_url = reverse_lazy('client:git')

    def form_valid(self, form):
        git = form.save()
        g = Github()
        name = form.cleaned_data.get("name")
        git.url = g.search_repositories(name)[0].url
        git.description = g.search_repositories(name)[0].description
        repo = g.get_repo(name)
        Commit.objects.all().delete()
        for commit in repo.get_commits():
            Commit.objects.create(sha=commit.sha, author=commit.author.email, comments=commit.commit.message,
                   date=commit.commit.committer.date, url=commit.url, git=git)
            print(commit.sha, commit.author.email, commit.commit.message, commit.commit.committer.date,
                  commit.commit.url)
        git.save()
        return super().form_valid(form)


class CommitCreateView(CreateView):
    model = Commit
    success_url = reverse_lazy('client:commit_list')
