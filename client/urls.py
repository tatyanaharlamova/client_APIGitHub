from django.urls import path
from client.apps import ClientConfig
from client.views import GitCreateView, CommitListView, GitListView

app_name = ClientConfig.name


urlpatterns = [
    path('', GitCreateView.as_view(), name='git_create'),
    path('git/', GitListView.as_view(), name='git'),
    path('commits-list/', CommitListView.as_view(), name='commits-list'),
]
