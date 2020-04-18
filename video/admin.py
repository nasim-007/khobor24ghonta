from django.contrib import admin
from video.models import VideoPost
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

class VideoPostAdmin(SummernoteModelAdmin):
    summernote_fields = ('video_content',)
    list_display = ('video_title', 'created_on', 'status')
    list_filter = ("status",)
    search_fields = ['video_content', ]

admin.site.register(VideoPost, VideoPostAdmin)