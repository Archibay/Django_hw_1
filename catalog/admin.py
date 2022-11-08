from django.contrib import admin
from .models import Logs


class LogsAdmin(admin.ModelAdmin):
    list_display = ['path', 'method', 'timestamp', 'values']
    list_filter = ['method']
    search_fields = ['path']
    ordering = ['-timestamp']
    list_per_page = 20
    fieldsets = (
        ('Log info', {
            'fields': ('path', 'method', 'values')
        }),
        ('Datetime log info', {
            'fields': ('timestamp',),
        }),
    )
    date_hierarchy = 'timestamp'
    save_as = True


admin.site.register(Logs, LogsAdmin)
