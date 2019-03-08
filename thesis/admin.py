from django.contrib import admin
from .models import Issue
from django.utils.text import wrap
# import easy
# from django.template.defaultfilters import linebreaksbr


class IssueAdmin(admin.ModelAdmin):
    search_fields = ['thesnr', 'description', 'prority', 'status', 'kind', 'sprint', 'storypoints']
    list_per_page = 15
    list_display = ('thesnr', 'shortDescription', 'priority', 'status', 'kind', 'sprint', 'storypoints')
    list_filter = ('priority', 'status', 'kind', 'sprint')


admin.site.register(Issue, IssueAdmin)

