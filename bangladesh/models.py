from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import math

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class BangladeshPost(models.Model):
    bangladesh_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='bangladesh_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(default='/static/images/postdefault.jpg', upload_to='images/')
    bangladesh_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    visit_bangladesh = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.bangladesh_title

    

    

    @property
    def comment_count(self):
        return BangladeshComment.objects.filter(bangladeshpost=self).count()






class BangladeshComment(models.Model):
    bangladeshpost = models.ForeignKey(BangladeshPost, on_delete= models.CASCADE, related_name='bangladesh_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies_bangladesh_comment')

    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.name