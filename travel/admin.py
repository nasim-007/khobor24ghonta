
from django.contrib import admin
from travel.models import TravelPost, TravelComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class TravelPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('travel_content',)
    
    list_display = ('travel_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['travel_content', 'travel_title'  ]
   

class TravelCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(TravelComment, TravelCommentAdmin)
admin.site.register(TravelPost, TravelPostAdmin)

