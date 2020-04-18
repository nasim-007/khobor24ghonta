from django.contrib import admin
from health.models import HealthPost, HealthComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class HealthPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('health_content',)
    
    list_display = ('health_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['health_content', 'health_title'  ]
   

class HealthCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(HealthComment, HealthCommentAdmin)
admin.site.register(HealthPost, HealthPostAdmin)

