from django.db import models

# Create your models here.

from django.conf import settings

from django.contrib.auth import get_user_model

from django.urls import reverse
from django_comments.models import Comment as CommentModel

from django_comments.moderation import CommentModerator, moderator # new

class Article(models.Model):
    
    title = models.CharField(max_length=255)
    
    body = models.TextField()
    
    date = models.DateTimeField(auto_now_add=True)
    
    author = models.ForeignKey(
        
        get_user_model(),
        
        on_delete=models.CASCADE,
        
    )
    
    def __str__(self):    
        
        return self.title
    
    def get_absolute_url(self):
        
        return reverse('article_detail', args=[str(self.id)])
    
    
class CustomComment(CommentModel): # new
    
    article = models.ForeignKey(
        
        Article, 
        
        on_delete=models.CASCADE,
        
        related_name='comments', # new
        
    )
    
    
    author = models.ForeignKey(
        
        get_user_model(),
        
        on_delete=models.CASCADE,
        
    )
    
    
    def __str__(self): 
        
        return self.comment

    
    def get_absolute_url(self):
        
        return reverse('article_list')
    

