from django.contrib import admin
from funny.models import FunnyPost, FunnyComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class FunnyPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('funny_content',)
    
    list_display = ('funny_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['funny_content', 'funny_title'  ]
   

class FunnyCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(FunnyComment, FunnyCommentAdmin)
admin.site.register(FunnyPost, FunnyPostAdmin)

