from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render

vue_urls = [
    path('', lambda request: HttpResponse(render(request, 'vue_index.html'))),
    path('about/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
    path('classify/', lambda request: HttpResponse(render(request, 'vue_index.html'))),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
    path('article/', include('article.urls')),
    path('', include(vue_urls))
]
