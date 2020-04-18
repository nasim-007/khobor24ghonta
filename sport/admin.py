
from django.contrib import admin
from sport.models import SportPost, SportComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class SportPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('sport_content',)
    
    list_display = ('sport_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['sport_content', 'sport_title'  ]
   

class SportCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(SportComment, SportCommentAdmin)
admin.site.register(SportPost, SportPostAdmin)

