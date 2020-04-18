from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)



class BreakingNews(models.Model):
    
    newscontent = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return self.newscontent


class Contact(models.Model):
    name = models.CharField(max_length=80)
    
    email = models.EmailField(max_length=200, blank=True)
    subject = models.CharField(max_length=80)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
   

    class Meta:
        # sort comments in chronological order by default
        ordering = ('created',)

    def __str__(self):
        return 'Contact by {}'.format(self.name)