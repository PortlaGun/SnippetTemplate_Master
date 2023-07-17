from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from MainApp import views


urlpatterns = [
    path('', views.index_page),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list', views.get_snippets, name='view_snippets_page'),
    path('snippet/1', views.get_snippet, name='view_snippet_page'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
