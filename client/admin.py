from django.contrib import admin

from client.models import Git, Commit


@admin.register(Git)
class GitAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'description')


@admin.register(Commit)
class CommitAdmin(admin.ModelAdmin):
    list_display = ('author', 'url', 'comments', 'date', 'sha', )
