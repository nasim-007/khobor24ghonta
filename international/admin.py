
from django.contrib import admin
from international.models import InternationalPost, InternationalComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class InternationalPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('international_content',)
    
    list_display = ('international_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['international_content', 'international_title'  ]
   

class InternationalCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(InternationalComment, InternationalCommentAdmin)
admin.site.register(InternationalPost, InternationalPostAdmin)

