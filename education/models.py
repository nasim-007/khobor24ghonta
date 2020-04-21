
from django.db import models
from django.contrib.auth.models import User


from django.utils import timezone
import math

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish"),
    (2,"Feature"),

)


class EducationPost(models.Model):
    education_title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='education_posts')
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(default='/static/images/postdefault.jpg', upload_to='images/')
    education_content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    visit_education = models.PositiveIntegerField(default=0)
    
    
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.education_title

    

    

    @property
    def comment_count(self):
        return EducationComment.objects.filter(educationpost=self).count()






class EducationComment(models.Model):
    educationpost = models.ForeignKey(EducationPost, on_delete= models.CASCADE, related_name='education_comments')
    name = models.CharField(max_length=80)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', on_delete= models.CASCADE, null=True, blank=True, related_name='replies_education_comment')

    
    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.name