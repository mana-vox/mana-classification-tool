from django.db import models


class Article(models.Model):
    id_article = models.IntegerField(unique=True)
    full_text = models.TextField()
    url = models.TextField()
    ids_ibm = models.JSONField(blank=True, null=True)


class Sentence(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    sentence_text = models.TextField()


class AccountArticle(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class AccountSentence(models.Model):
    account = models.ForeignKey('account.Account', on_delete=models.CASCADE)
    sentence = models.ForeignKey(Sentence, on_delete=models.CASCADE)
    label = models.IntegerField()
