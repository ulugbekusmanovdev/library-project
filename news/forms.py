from django import forms
from django.forms import ModelForm

from .models import *


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'text', 'image']
