
from django.contrib import admin
from bangladesh.models import BangladeshPost, BangladeshComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class BangladeshPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('bangladesh_content',)
    
    list_display = ('bangladesh_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['bangladesh_content', 'bangladesh_title'  ]
   

class BangladeshCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(BangladeshComment, BangladeshCommentAdmin)
admin.site.register(BangladeshPost, BangladeshPostAdmin)
