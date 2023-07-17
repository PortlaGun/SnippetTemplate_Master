from django.http import Http404
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.http import HttpResponseRedirect, HttpResponseNotFound

def index_page(request):
    context = {'pagename': 'PythonBin'}
    return render(request, 'pages/index.html', context)


def add_snippet_page(request):
    context = {'pagename': 'Добавление нового сниппета'}
    return render(request, 'pages/add_snippet.html', context)


def snippets_page(request):
    context = {'pagename': 'Просмотр сниппетов'}
    return render(request, 'pages/view_snippets.html', context)


def create_snippet(request):
   form = SnippetForm()
   return render(request, 'add_snippet.html', {'form': form})


# получение данных из бд
def get_snippets(request):
    snippets = Snippet.objects.all()
    for snippet in snippets:
        snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    context = {"snippets": snippets, "hide": False}
    return render(request, "pages/view_snippets.html", context)

def get_snippet(request):
    # try:
    #     snippet = Snippet.objects.get(id=request.GET.get("snippet_id"))
    #     snippet.creation_date = snippet.creation_date.strftime("%Y-%m-%d %H:%M")
    #     context = {'snippet': snippet}
    #     return render(request, "pages/view_snippet.html", context)
    # except Snippet.DoesNotExist:
    #     return HttpResponseNotFound("<h2>snippet not found</h2>")
    context = {'snippet': 'snippet'}
    return render(request, "pages/view_snippet.html", context)