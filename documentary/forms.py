from django import forms
from .models import Documentary, Comment, Reply

class DocumentaryForm(forms.ModelForm):
    class Meta:
        model = Documentary
        fields = ['title', 'description', 'year', 'author', 'pdf']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']