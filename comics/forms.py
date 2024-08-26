from django import forms
from .models import Comic, ComicImage

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class ComicForm(forms.ModelForm):
    class Meta:
        model = Comic
        fields = ['title', 'cover_image']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Create Comic', css_class='btn-primary'))


class ComicImageForm(forms.ModelForm):
    class Meta:
        model = ComicImage
        fields = ['image', 'description']
