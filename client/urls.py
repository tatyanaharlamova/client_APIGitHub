from django.urls import path
from client.apps import ClientConfig
from client.views import GitDetailView, GitCreateView, CommitListView

app_name = ClientConfig.name


urlpatterns = [
    path('', GitCreateView.as_view(), name='git_create'),
    path('git_detail/', GitDetailView.as_view(), name='git_detail'),
    path('commits_list/', CommitListView.as_view(), name='commits_list'),
]
