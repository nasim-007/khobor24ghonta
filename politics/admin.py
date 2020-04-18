from django.contrib import admin
from politics.models import PoliticsPost, PoliticsComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class PoliticsPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('politics_content',)
    
    list_display = ('politics_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['politics_content', 'politics_title'  ]
   

class PoliticsCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(PoliticsComment, PoliticsCommentAdmin)
admin.site.register(PoliticsPost, PoliticsPostAdmin)
