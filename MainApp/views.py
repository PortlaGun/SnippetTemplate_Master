from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.views.decorators.csrf import requires_csrf_token
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import UserRegisterForm
from MainApp.models import Snippet, Profile


def index_page(request):
    context = {'pagename': 'SnippetPile'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


# получение данных из бд
def get_snippets(request):
    snippets = Snippet.objects.filter(hide=False, is_public=True)
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {"snippets": snippets, "hide": False}
    return render(request, "pages/view_snippets.html", context)


def get_snippets_hide(request):
    snippets = Snippet.objects.filter(is_public=True)
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {"snippets": snippets, "hide": True}
    return render(request, "pages/view_snippets.html", context)


@requires_csrf_token
def make_hidden_or_show(request, id):
    snippet = Snippet.objects.get(id=id)
    if snippet.hide:
        snippet.hide = False
    else:
        snippet.hide = True
    snippet.save()
    return HttpResponseRedirect("/snippets/list")


# сохранение данных в бд
@requires_csrf_token
def create_snippet(request):
    if request.method == "POST":
        snippet = Snippet()
        user = User.objects.get(id=request.user.id)
        snippet.name = request.POST.get("name")
        snippet.lang = request.POST.get("lang")
        snippet.code = request.POST.get("code")
        if request.POST.get("pub") == 'pub':
            snippet.is_public = True
        else:
            snippet.is_public = False
        snippet.author = user
        snippet.save()
        messages.success(request, f'Создан сниппет {snippet.name}!')
    return HttpResponseRedirect("/")


def get_snippet_for_update(request, id):
    snippet = Snippet.objects.get(id=id)
    snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {'snippet': snippet}
    return render(request, "pages/update_snippet.html", context)


def update_snippet(request):
    snippet = Snippet.objects.get(id=request.POST.get("id"))

    snippet.name = request.POST.get("name")
    snippet.lang = request.POST.get("lang")
    snippet.code = request.POST.get("code")
    if request.POST.get("pub") == 'pub':
        snippet.is_public = True
    else:
        snippet.is_public = False
    snippet.save()
    messages.success(request, f'Cниппет {snippet.name} подвергся редактированию!')
    return HttpResponseRedirect("/")


def delete_snippet(request, id):
    try:
        snippet = Snippet.objects.get(id=id)
        snippet.delete()
        messages.success(request, f'Cниппет {snippet.name} удален!')
        return HttpResponseRedirect("/")
    except Snippet.DoesNotExist:
        return HttpResponseNotFound("<h2>snippet not found</h2>")


def get_snippet(request):
    try:
        snippet = Snippet.objects.get(id=request.GET.get("snippet_id"), hide=False, is_public=True)
        snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
        context = {'snippet': snippet}
        return render(request, "pages/view_snippet.html", context)
    except Snippet.DoesNotExist:
        return HttpResponseNotFound("<h2>snippet not found</h2>")


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Создан аккаунт {username}!')
            return redirect('/')
    else:
        form = UserRegisterForm()
    return render(request, 'pages/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'pages/profile.html')


def my_snippets(request):
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        snippets = Snippet.objects.filter(author=user)
        print(snippets)
        context = {"snippets": snippets}
        return render(request, "pages/my_snippets.html", context)
    else:
        return HttpResponseRedirect("/login")

