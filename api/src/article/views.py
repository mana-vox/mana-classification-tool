
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from .models import Article


@api_view(['POST'])
@permission_classes([IsAdminUser])
def new_article_view(request):
    article = Article(id_article=request.data['id_article'],
                      full_text=request.data['full_text'], url=request.data['url'])
    article.save()
    data = {'article': 'Successfully created a new article'}
    status_code = status.HTTP_201_CREATED
    return Response(status=status_code, data=data)
