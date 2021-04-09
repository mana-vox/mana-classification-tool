
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Article, Sentence


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
