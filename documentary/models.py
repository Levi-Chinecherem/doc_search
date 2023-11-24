from django.db import models
from django.contrib.auth.models import User

class Documentary(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    year = models.IntegerField()
    pdf = models.FileField(upload_to='documents/')

    class Meta:
        ordering = ['-id']
        
    def __str__(self):
        return self.title

class Comment(models.Model):
    documentary = models.ForeignKey(Documentary, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.documentary.title}'

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Reply by {self.user.username} to {self.comment}'
