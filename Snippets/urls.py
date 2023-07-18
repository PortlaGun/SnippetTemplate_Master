from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from MainApp import views

urlpatterns = [
    path('', views.index_page),
    path('snippets/add', views.add_snippet_page, name='add_snippet_page'),
    path('snippets/list', views.get_snippets, name='snippets_page'),
    path('snippets/list_hide', views.get_snippets_hide, name='snippets_page_hide'),
    path('snippets/make_hidden_or_show/<int:id>', views.make_hidden_or_show, name='make_hidden_or_show'),
    path('snippets/', views.get_snippet, name='snippet_page'),
    path('snippets/my_snippets', views.my_snippets, name='my_snippets'),
    path("snippets/create", views.create_snippet, name='snippet_create'),
    path('snippets/delete/<int:id>', views.delete_snippet, name='snippet_delete'),
    path('snippets/edit/<int:id>', views.get_snippet_for_update, name='snippet_edit'),
    path('snippets/update', views.update_snippet, name='snippet_update'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='pages/logout.html'), name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
