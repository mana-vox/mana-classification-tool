from .models import AccountArticle, AccountSentence, Sentence


def is_classified(article):
    account_articles = AccountArticle.objects.filter(article=article)
    if account_articles.count() >= 3:
        return True
    else:
        if account_articles.count() == 1:
            return False
        elif account_articles.count() == 2:
            account_1 = account_articles[0]
            account_2 = account_articles[1]
            for sentence in Sentence.objects.filter(article=article):
                if (AccountSentence.objects.filter(account=account_1).filter(sentence=sentence).label !=
                        AccountSentence.objects.filter(account=account_2).filter(sentence=sentence).label):
                    return False
            return True
        else:
            return False
