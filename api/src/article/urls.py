from django.urls import path

from .views import new_article_view


app_name = 'article'

urlpatterns = [
    path('new', new_article_view, name='new_article')
]
