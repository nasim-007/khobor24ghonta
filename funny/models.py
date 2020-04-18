from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone
import math

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class FunnyPost(models.Model):
    funny_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='funny_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='images/')
    funny_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    visit_funny = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.funny_title

    

    

    @property
    def comment_count(self):
        return FunnyComment.objects.filter(funnypost=self).count()






class FunnyComment(models.Model):
    funnypost = models.ForeignKey(FunnyPost, on_delete= models.CASCADE, related_name='funny_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies_funny_comment')

    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.name
