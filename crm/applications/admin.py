from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated', 'payments',)
    fieldsets = [
        ('Main information', {
            'fields': ['name', 'agreement_id', 'created', 'updated']
        }),
        ('Payments', {
            'fields': ['payments', ]}),
            ]


admin.site.register(Application, ApplicationAdmin)
