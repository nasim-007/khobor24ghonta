
from django.contrib import admin
from fashion.models import FashionPost, FashionComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class FashionPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('fashion_content',)
    
    list_display = ('fashion_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['fashion_content', 'fashion_title'  ]
   

class FashionCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(FashionComment, FashionCommentAdmin)
admin.site.register(FashionPost, FashionPostAdmin)

