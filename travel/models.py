
from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import math

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)


class TravelPost(models.Model):
    travel_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='travel_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(default='/static/images/postdefault.jpg', upload_to='images/')
    travel_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    visit_travel = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.travel_title

    

    

    @property
    def comment_count(self):
        return TravelComment.objects.filter(travelpost=self).count()






class TravelComment(models.Model):
    travelpost = models.ForeignKey(TravelPost, on_delete= models.CASCADE, related_name='travel_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies_travel_comment')

    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.name
