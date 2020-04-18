from django.contrib import admin
from technology.models import TechnologyPost, TechnologyComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class TechnologyPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('technology_content',)
    
    list_display = ('technology_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['technology_content', 'technology_title'  ]
   

class TechnologyCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(TechnologyComment, TechnologyCommentAdmin)
admin.site.register(TechnologyPost, TechnologyPostAdmin)
