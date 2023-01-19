from modeltranslation.translator import register, TranslationOptions

from .models import *


@register(Ads)
class AdsTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Library)
class LibraryTranslationOptions(TranslationOptions):
    fields = ('l_title', 'l_body', 'm_title', 'm_body', 'os_title', 'os_body', 'history_title', 'history_body')


@register(Photo)
class PhotoTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Catalog)
class CatalogTranslationOptions(TranslationOptions):
    fields = ('c_title', 'c_body',)


@register(Readers)
class ReadersTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)


@register(Contact)
class ContactTranslationOptions(TranslationOptions):
    fields = ('title', 'text',)