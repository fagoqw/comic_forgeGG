from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Comic, ComicImage, Comment

class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'cover_image', 'description', 'tags']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create Comic', css_class='btn-primary'))

class ComicImageForm(forms.ModelForm):
    class Meta:
        model = ComicImage
        fields = ['image', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
