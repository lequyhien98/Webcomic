from django import forms
from .models import Post, Comment
from django.contrib.auth.models import User
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = [
            'reporting_url',
            'message'
        ]
        
class CommentForm(forms.ModelForm):
    content = forms.CharField(label="", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Text goes here!!!', 'rows':'4', 'cols':'50'}))
    class Meta:
        model = Comment
        fields = ('content',)
