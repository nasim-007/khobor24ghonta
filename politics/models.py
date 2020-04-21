from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import math

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class PoliticsPost(models.Model):
    politics_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='politics_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(default='/static/images/postdefault.jpg', upload_to='images/')
    politics_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    visit_politics = models.PositiveIntegerField(default=0)
   
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.politics_title

    

    

    @property
    def comment_count(self):
        return PoliticsComment.objects.filter(politicspost=self).count()






class PoliticsComment(models.Model):
    politicspost = models.ForeignKey(PoliticsPost, on_delete= models.CASCADE, related_name='politics_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies')

    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.name