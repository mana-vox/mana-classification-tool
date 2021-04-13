from django.contrib import admin

from .models import Article, Sentence, AccountArticle, AccountSentence


admin.site.register(Article)
admin.site.register(Sentence)
admin.site.register(AccountArticle)
admin.site.register(AccountSentence)
