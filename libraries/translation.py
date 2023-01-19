from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Library)
class LibraryTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)