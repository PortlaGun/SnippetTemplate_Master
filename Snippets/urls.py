from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from MainApp import views


urlpatterns = [0
    path('', views.index_page),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list', views.snippets_page, name='view_snippets_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)