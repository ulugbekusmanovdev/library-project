from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)