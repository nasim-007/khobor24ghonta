from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)



class VideoPost(models.Model):
    video_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    video_content = models.TextField()
    video_description = models.TextField( blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    visitor_video = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.video_title
