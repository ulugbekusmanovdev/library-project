from django import forms
from django.forms import ModelForm
from ckeditor.widgets import CKEditorWidget
from .models import *


class NewsForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = News
        fields = ['title', 'text', 'image']
