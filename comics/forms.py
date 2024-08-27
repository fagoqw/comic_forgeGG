from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Comic, ComicImage, Comment

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'description', 'cover_image']

class ComicImageForm(forms.ModelForm):
    class Meta:
        model = ComicImage
        fields = ['image', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
