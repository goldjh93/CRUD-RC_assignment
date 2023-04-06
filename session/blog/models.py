from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    def __str__(self):
        return self.title
    
    def summary(self):
        return self.content[:100]
    
# class Search(models.Model):
#     title_word = models.CharField(max_length=100)
#     content_word = models.CharField(max_length=100)

#     def __str__(self):
#         return self.title_word