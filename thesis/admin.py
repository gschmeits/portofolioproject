from django.contrib import admin
from .models import Issue


class IssueAdmin(admin.ModelAdmin):
    search_fields = ['tesnr']
    list_per_page = 20
    list_display = ('thesnr', 'description', 'status', 'kind', 'sprint')
    list_filter = ('status', 'kind')


admin.site.register(Issue, IssueAdmin)

