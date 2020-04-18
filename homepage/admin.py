from django.contrib import admin
from homepage.models import BreakingNews, Contact
# Register your models here.

class BreakingNewsAdmin(admin.ModelAdmin):
    list_display = ('newscontent', 'created', 'status')
    list_filter = ("status",)
    search_fields = ['newscontent', ]

admin.site.register(BreakingNews, BreakingNewsAdmin)
admin.site.register(Contact)