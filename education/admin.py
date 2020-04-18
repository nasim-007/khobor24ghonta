
from django.contrib import admin
from education.models import EducationPost, EducationComment

from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class EducationPostAdmin(SummernoteModelAdmin):
    
    summernote_fields = ('education_content',)
    
    list_display = ('education_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['education_content', 'education_title'  ]
   

class EducationCommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'body')
    search_fields = ['name', 'email'  ]

admin.site.register(EducationComment, EducationCommentAdmin)
admin.site.register(EducationPost, EducationPostAdmin)
