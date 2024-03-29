from django import forms

from . import models


class BlogCreationForm(forms.ModelForm):

    class Meta:
        model = models.BlogPost
        fields = ['title', 'content']


class BlogUpdationForm(forms.ModelForm):

    class Meta:
        model = models.BlogPost
        fields = ['title', 'content', 'status']
