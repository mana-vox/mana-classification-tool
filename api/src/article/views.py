
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from .models import Article, Sentence, AccountArticle, AccountSentence
from account.models import Account


@api_view(['POST'])
@permission_classes([IsAdminUser])
def new_article_view(request):
    article = Article(id_article=request.data['id_article'],
                      full_text=request.data['full_text'], url=request.data['url'])
    article.save()
    list_sentences = request.data['full_text'].split('.')
    list_sentences_exclamation = []
    for sentence in list_sentences:
        sub_list_sentences = sentence.split('!')
        for sub_sentence in sub_list_sentences:
            list_sentences_exclamation.append(sub_sentence)
    list_sentences_interrogation = []
    for sentence in list_sentences_exclamation:
        sub_list_sentences = sentence.split('?')
        for sub_sentence in sub_list_sentences:
            list_sentences_interrogation.append(sub_sentence)
    final_lists = []
    for sentence in list_sentences_interrogation:
        final_lists.append(sentence.lstrip().rstrip())
    for sentence in final_lists:
        if sentence != '':
            sentence_object = Sentence(article=article, sentence_text=sentence)
            sentence_object.save()
    data = {'article': 'Successfully created a new article'}
    status_code = status.HTTP_201_CREATED
    return Response(status=status_code, data=data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def classify_article_view(request):
    account = Account.objects.get(email=request.user.email)
    for sentence in request.data['sentences']:
        sentence_id = int(list(sentence.keys())[0])
        sentence_object = Sentence.objects.get(id=sentence_id)
        label = sentence[str(sentence_id)] == 'OUI_MANA'
        account_sentence = AccountSentence(account=account, sentence=sentence_object, label=label)
        account_sentence.save()
    article = sentence_object.article
    account_article = AccountArticle(account=account, article=article)
    account_article.save()
    data = {'classify': 'Successfully classified the article'}
    return Response(status=status.HTTP_200_OK, data=data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_article_view(request):
    account = Account.objects.get(email=request.user.email)
    classified_articles_ids = [el['article_id'] for el in list(
        AccountArticle.objects.filter(account=account).values('article_id'))]
    articles_not_classified = Article.objects.exclude(id__in=classified_articles_ids)
    for article in articles_not_classified:
        if AccountArticle.objects.filter(article=article).count() <= 2:
            sentences = []
            for sentence in Sentence.objects.filter(article=article):
                sentence_data = {
                    'id': sentence.id,
                    'sentence_text': sentence.sentence_text
                }
                sentences.append(sentence_data)
            data = {
                'sentences': sentences
            }
            return Response(status=status.HTTP_200_OK, data=data)
    return Response(status=status.HTTP_404_NOT_FOUND, data={})
