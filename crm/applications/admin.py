from django.contrib import admin

from .models import Application


class ApplicationAdmin(admin.ModelAdmin):
    suit_form_tabs = (('general', 'General'), ('payments', 'Payments'))
    readonly_fields = ('created', 'updated', 'payments',)
    fieldsets = [
        ('Main information', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': ['name', 'agreement_id', 'created', 'updated']
        }),
        ('Payments', {
            'classes': ('suit-tab', 'suit-tab-payments',),
            'fields': ['payments', ]}),
            ]


admin.site.register(Application, ApplicationAdmin)
