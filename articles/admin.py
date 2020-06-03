from django.contrib import admin

# Register your models here.

from .models import Article, CustomComment # new

class CommentInline(admin.TabularInline): # new
    
    model = CustomComment
    
class ArticleAdmin(admin.ModelAdmin): # new
    
    inlines = [
        
        CommentInline,
    
    ]

admin.site.register(Article, ArticleAdmin) # new

admin.site.register(CustomComment) # new