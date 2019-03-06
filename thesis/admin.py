from django.contrib import admin
from .models import Issue


class IssueAdmin(admin.ModelAdmin):
    search_fields = ['thesnr', 'description']
    list_per_page = 15
    list_display = ('thesnr', 'description', 'priority', 'status', 'kind', 'sprint')
    list_filter = ('priority', 'status', 'kind')


admin.site.register(Issue, IssueAdmin)

